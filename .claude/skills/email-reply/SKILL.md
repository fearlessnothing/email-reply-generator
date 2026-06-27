# Email Reply Generator Skill

Generate professional email replies using AI.

## Inputs

- **email** (required): The email content to reply to
- **tone** (optional): Reply tone - `formal`, `friendly`, or `short` (default: `formal`)

## Output

A generated email reply that:
- Addresses the sender's main points
- Matches the requested tone
- Is concise and professional

## Usage

```bash
python main.py --email "Your email content" --tone friendly
```

## Environment

Requires `API_KEY` in `.env` file. See `.env.example`.
