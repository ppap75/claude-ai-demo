# Claude AI Demo Project

A Python project demonstrating how to interact with Anthropic's Claude AI API, including both a CLI demo and a REST API with Docker support.

## Features

### CLI Demo (`main.py`)
Three examples showing different ways to use Claude:
1. **Simple Question**: Basic single-turn conversation with Claude
2. **Multi-turn Conversation**: Maintaining context across multiple exchanges
3. **Custom System Prompt**: Using system prompts to customize Claude's behavior

### REST API (`api.py`)
FastAPI-based REST API with the following endpoints:
- `POST /chat` - Send a single message to Claude
- `POST /conversation` - Send multi-turn conversations
- `GET /health` - Health check endpoint
- `GET /models` - List available Claude models
- Interactive API documentation at `/docs`

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

## Running the Project

### Option 1: CLI Demo

Execute the main script:

```bash
python main.py
```

### Option 2: REST API (Local)

Start the FastAPI server:

```bash
python api.py
```

Or using uvicorn directly:

```bash
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Option 3: Docker Container

Build and run using Docker:

```bash
# Build the image
docker build -t claude-ai-api .

# Run the container
docker run -p 8000:8000 --env-file .env claude-ai-api
```

### Option 4: Docker Compose (Recommended)

The easiest way to run the API:

```bash
# Start the service
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the service
docker-compose down
```

The API will be available at http://localhost:8000

## What the Demo Does

The script demonstrates three different ways to use the Claude API:

### Example 1: Simple Question
A straightforward single-question interaction asking about the capital of France.

### Example 2: Multi-turn Conversation
Shows how to maintain conversation context by building a message history, allowing Claude to remember previous exchanges.

### Example 3: Custom System Prompt
Demonstrates using system prompts to customize Claude's response style (in this case, explaining concepts with simple analogies).

## API Usage Examples

### Using curl

**Simple chat:**
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the capital of France?"}'
```

**With custom model and system prompt:**
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Explain recursion",
    "model": "claude-4-5-sonnet-20241022",
    "max_tokens": 2048,
    "system_prompt": "You are a patient teacher who uses simple analogies."
  }'
```

**Multi-turn conversation:**
```bash
curl -X POST "http://localhost:8000/conversation" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello! Can you help me?"},
      {"role": "assistant", "content": "Of course! I am happy to help."},
      {"role": "user", "content": "What is Python?"}
    ]
  }'
```

### Using Python

```python
import requests

# Simple chat
response = requests.post(
    "http://localhost:8000/chat",
    json={"message": "What is the capital of France?"}
)
print(response.json())

# Multi-turn conversation
response = requests.post(
    "http://localhost:8000/conversation",
    json={
        "messages": [
            {"role": "user", "content": "Hello!"},
            {"role": "assistant", "content": "Hi! How can I help?"},
            {"role": "user", "content": "Tell me about Python"}
        ]
    }
)
print(response.json())
```

## Project Structure

```
vscode_dev/
├── .github/
│   └── copilot-instructions.md  # Project documentation for Copilot
├── .venv/                        # Virtual environment (not in repo)
├── .env                          # Your API key (not in repo)
├── .env.example                  # Template for environment variables
├── .dockerignore                 # Docker ignore rules
├── .gitignore                    # Git ignore rules
├── api.py                        # FastAPI REST API
├── docker-compose.yml            # Docker Compose configuration
├── Dockerfile                    # Docker container definition
├── main.py                       # CLI demo script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Available Claude Models

This project uses `claude-4-5-sonnet-20241022` by default, which is the latest and most capable Sonnet model. Other available models include:
- `claude-4-5-sonnet-20241022` - Latest Sonnet model (default)
- `claude-3-5-sonnet-20241022` - Previous Sonnet model
- `claude-3-opus-20240229` - Most capable, best for complex tasks
- `claude-3-sonnet-20240229` - Balanced performance and speed
- `claude-3-haiku-20240307` - Fastest, best for simple tasks

You can list all available models by calling `GET /models` endpoint.

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
