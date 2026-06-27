# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Email Reply Generator - a Python CLI tool that generates professional email replies using OpenAI's API.

## Project Structure

```
email-reply-generator/
├── main.py              # CLI entry point
├── requirements.txt     # Python dependencies
├── prompts/
│   └── reply_prompt.txt # Prompt template for reply generation
└── .env                 # Environment variables (create this, not in git)
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

Generate a reply from inline text:
```bash
python main.py --email "Your email content here"
```

Generate a reply from a file:
```bash
python main.py --file email.txt
```

Generate a reply from stdin:
```bash
echo "Email content" | python main.py
```

## Architecture

- **main.py**: CLI interface using Click. Handles input parsing, API calls, and output formatting.
- **prompts/reply_prompt.txt**: Template for the AI prompt. Uses `{email_content}` placeholder for variable substitution.
- Uses OpenAI's GPT-3.5-turbo model for generating replies.
