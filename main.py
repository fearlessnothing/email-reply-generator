#!/usr/bin/env python3
"""Email Reply Generator - CLI tool to generate email replies."""

import os
import sys
from pathlib import Path

import click
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROMPTS_DIR = Path(__file__).parent / "prompts"
VALID_TONES = ["formal", "friendly", "short"]


def get_api_key() -> str:
    """Get API key from environment variable."""
    api_key = os.getenv("API_KEY")
    if not api_key:
        click.echo("Error: API_KEY environment variable not set.", err=True)
        click.echo("Create a .env file based on .env.example.", err=True)
        sys.exit(1)
    return api_key


def load_prompt_template() -> str:
    """Load the reply prompt template from file."""
    prompt_path = PROMPTS_DIR / "reply_prompt.txt"
    if not prompt_path.exists():
        click.echo("Error: Prompt template not found.", err=True)
        sys.exit(1)
    return prompt_path.read_text()


def format_prompt(email_content: str, tone: str) -> str:
    """Format the prompt template with email content and tone."""
    template = load_prompt_template()
    return template.format(tone=tone, email_content=email_content)


def get_email_input(email: str, file_path: str) -> str:
    """Get email content from argument, file, or stdin."""
    if file_path:
        return Path(file_path).read_text()
    elif email:
        return email
    elif not sys.stdin.isatty():
        return sys.stdin.read()
    else:
        click.echo("Error: Provide email via --email, --file, or stdin.", err=True)
        sys.exit(1)


def generate_reply(prompt: str, api_key: str) -> str:
    """Generate email reply using OpenAI API."""
    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful email assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=500,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        click.echo(f"Error calling API: {e}", err=True)
        sys.exit(1)


@click.command()
@click.option("--email", "-e", help="Email content to reply to.")
@click.option("--file", "-f", "file_path", type=click.Path(exists=True), help="File containing email content.")
@click.option("--tone", "-t", type=click.Choice(VALID_TONES), default="formal", help="Reply tone.")
def main(email: str, file_path: str, tone: str):
    """Generate professional email replies using AI."""
    api_key = get_api_key()
    email_content = get_email_input(email, file_path)

    if not email_content.strip():
        click.echo("Error: Email content is empty.", err=True)
        sys.exit(1)

    prompt = format_prompt(email_content, tone)

    click.echo(f"Generating {tone} reply...\n")
    reply = generate_reply(prompt, api_key)
    click.echo(reply)


if __name__ == "__main__":
    main()
