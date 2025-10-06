# Claude AI Demo Project

A Python demonstration project showing how to interact with Anthropic's Claude AI API.

## Features

This demo includes three examples:
1. **Simple Question**: Basic single-turn conversation with Claude
2. **Multi-turn Conversation**: Maintaining context across multiple exchanges
3. **Custom System Prompt**: Using system prompts to customize Claude's behavior

## Prerequisites

- Python 3.11 or higher
- An Anthropic API key (get one at https://console.anthropic.com/)

## Setup Instructions

### 1. Clone or Navigate to This Project

```bash
cd vscode_dev
```

### 2. Create a Virtual Environment (Already configured)

A virtual environment has been set up for this project.

### 3. Install Dependencies

The required packages have been installed:
- `anthropic` - Official Anthropic Python SDK
- `python-dotenv` - For environment variable management

To reinstall if needed:
```bash
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Configure Your API Key

1. Copy the `.env.example` file to create a new `.env` file:
   ```bash
   copy .env.example .env
   ```

2. Edit the `.env` file and replace `your_api_key_here` with your actual Anthropic API key:
   ```
   ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
   ```

**Important**: Never commit your `.env` file to version control. It's already listed in `.gitignore`.

## Running the Demo

Execute the main script:

```bash
.venv\Scripts\python.exe main.py
```

Or simply:

```bash
python main.py
```

## What the Demo Does

The script demonstrates three different ways to use the Claude API:

### Example 1: Simple Question
A straightforward single-question interaction asking about the capital of France.

### Example 2: Multi-turn Conversation
Shows how to maintain conversation context by building a message history, allowing Claude to remember previous exchanges.

### Example 3: Custom System Prompt
Demonstrates using system prompts to customize Claude's response style (in this case, explaining concepts with simple analogies).

## Project Structure

```
vscode_dev/
├── .github/
│   └── copilot-instructions.md  # Project documentation for Copilot
├── .venv/                        # Virtual environment (not in repo)
├── .env                          # Your API key (not in repo)
├── .env.example                  # Template for environment variables
├── .gitignore                    # Git ignore rules
├── main.py                       # Main demo script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## API Models

This demo uses `claude-3-5-sonnet-20241022`, which is one of Anthropic's most capable models. Other available models include:
- `claude-3-opus-20240229` - Most capable, best for complex tasks
- `claude-3-sonnet-20240229` - Balanced performance and speed
- `claude-3-haiku-20240307` - Fastest, best for simple tasks

## Error Handling

The script includes error handling for common issues:
- Missing API key
- API connection problems
- Invalid responses

## Learn More

- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Claude API Reference](https://docs.anthropic.com/claude/reference/)
- [Python SDK on GitHub](https://github.com/anthropics/anthropic-sdk-python)

## License

This is a demo project for educational purposes.
