#!/usr/bin/env python3
"""Email Reply Generator - CLI tool to generate email replies."""

import sys
from pathlib import Path

import click

PROMPTS_DIR = Path(__file__).parent / "prompts"
VALID_TONES = ["formal", "friendly", "short"]


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


def generate_mock_reply(prompt: str) -> str:
    """Generate a mock reply (placeholder for API integration)."""
    return (
        "Thank you for your email. I have received your message and will "
        "get back to you shortly.\n\n"
        "Best regards,\n[Your Name]"
    )


@click.command()
@click.option("--email", "-e", help="Email content to reply to.")
@click.option("--file", "-f", "file_path", type=click.Path(exists=True), help="File containing email content.")
@click.option("--tone", "-t", type=click.Choice(VALID_TONES), default="formal", help="Reply tone.")
def main(email: str, file_path: str, tone: str):
    """Generate professional email replies using AI."""
    email_content = get_email_input(email, file_path)

    if not email_content.strip():
        click.echo("Error: Email content is empty.", err=True)
        sys.exit(1)

    prompt = format_prompt(email_content, tone)

    click.echo(f"Generating {tone} reply...\n")
    reply = generate_mock_reply(prompt)
    click.echo(reply)


if __name__ == "__main__":
    main()
