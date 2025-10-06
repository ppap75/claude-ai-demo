"""
Claude AI API
FastAPI application to expose Claude AI functionality through REST endpoints.
"""

import os
from typing import Optional, List
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Claude AI API",
    description="REST API for interacting with Anthropic's Claude AI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Anthropic client
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

client = Anthropic(api_key=api_key)


# Pydantic models
class Message(BaseModel):
    role: str = Field(..., description="Role: 'user' or 'assistant'")
    content: str = Field(..., description="Message content")


class ChatRequest(BaseModel):
    message: str = Field(..., description="User message to send to Claude")
    model: str = Field(default="claude-sonnet-4-5-20250929", description="Claude model to use")
    max_tokens: int = Field(default=1024, ge=1, le=4096, description="Maximum tokens in response")
    system_prompt: Optional[str] = Field(None, description="Optional system prompt")


class ConversationRequest(BaseModel):
    messages: List[Message] = Field(..., description="List of conversation messages")
    model: str = Field(default="claude-sonnet-4-5-20250929", description="Claude model to use")
    max_tokens: int = Field(default=1024, ge=1, le=4096, description="Maximum tokens in response")
    system_prompt: Optional[str] = Field(None, description="Optional system prompt")


class ChatResponse(BaseModel):
    response: str = Field(..., description="Claude's response")
    model: str = Field(..., description="Model used")
    tokens_used: int = Field(..., description="Number of tokens used")


# API endpoints
@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "Claude AI API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "POST /chat": "Send a single message to Claude",
            "POST /conversation": "Send a multi-turn conversation to Claude",
            "GET /health": "Health check endpoint",
            "GET /models": "List available Claude models"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "api_key_configured": bool(api_key)
    }


@app.get("/models")
async def list_models():
    """List available Claude models."""
    return {
        "models": [
            {
                "id": "claude-sonnet-4-5-20250929",
                "name": "Claude Sonnet 4.5",
                "description": "Latest and most capable Sonnet model"
            },
            {
                "id": "claude-3-5-sonnet-20241022",
                "name": "Claude 3.5 Sonnet",
                "description": "Previous Sonnet model"
            },
            {
                "id": "claude-3-opus-20240229",
                "name": "Claude 3 Opus",
                "description": "Most capable, best for complex tasks"
            },
            {
                "id": "claude-3-sonnet-20240229",
                "name": "Claude 3 Sonnet",
                "description": "Balanced performance and speed"
            },
            {
                "id": "claude-3-haiku-20240307",
                "name": "Claude 3 Haiku",
                "description": "Fastest, best for simple tasks"
            }
        ]
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a single message to Claude and get a response.
    
    - **message**: The message to send to Claude
    - **model**: Claude model to use (default: claude-sonnet-4-5-20250929)
    - **max_tokens**: Maximum tokens in response (default: 1024)
    - **system_prompt**: Optional system prompt to customize behavior
    """
    try:
        kwargs = {
            "model": request.model,
            "max_tokens": request.max_tokens,
            "messages": [{"role": "user", "content": request.message}]
        }
        
        if request.system_prompt:
            kwargs["system"] = request.system_prompt
        
        response = client.messages.create(**kwargs)
        
        return ChatResponse(
            response=response.content[0].text,
            model=response.model,
            tokens_used=response.usage.input_tokens + response.usage.output_tokens
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error communicating with Claude: {str(e)}"
        )


@app.post("/conversation", response_model=ChatResponse)
async def conversation(request: ConversationRequest):
    """
    Send a multi-turn conversation to Claude.
    
    - **messages**: List of messages with role and content
    - **model**: Claude model to use (default: claude-sonnet-4-5-20250929)
    - **max_tokens**: Maximum tokens in response (default: 1024)
    - **system_prompt**: Optional system prompt to customize behavior
    """
    try:
        # Convert Pydantic models to dicts
        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]
        
        kwargs = {
            "model": request.model,
            "max_tokens": request.max_tokens,
            "messages": messages
        }
        
        if request.system_prompt:
            kwargs["system"] = request.system_prompt
        
        response = client.messages.create(**kwargs)
        
        return ChatResponse(
            response=response.content[0].text,
            model=response.model,
            tokens_used=response.usage.input_tokens + response.usage.output_tokens
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error communicating with Claude: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
