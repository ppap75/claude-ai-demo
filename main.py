"""
Claude AI Demo
This script demonstrates how to interact with Anthropic's Claude AI API.
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv


def main():
    """Main function to demonstrate Claude API usage."""
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment variable
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    print(api_key)
    
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key (see .env.example)")
        return
    
    # Initialize the Anthropic client
    client = Anthropic(api_key=api_key)
    
    # Example 1: Simple conversation
    print("=" * 60)
    print("Example 1: Simple Question")
    print("=" * 60)
    
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )
    
    print(f"Claude: {message.content[0].text}\n")
    
    # Example 2: Multi-turn conversation
    print("=" * 60)
    print("Example 2: Multi-turn Conversation")
    print("=" * 60)
    
    conversation = [
        {"role": "user", "content": "Hello! Can you help me with Python programming?"},
    ]
    
    response1 = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=conversation
    )
    
    print(f"User: {conversation[0]['content']}")
    print(f"Claude: {response1.content[0].text}\n")
    
    # Continue the conversation
    conversation.append({"role": "assistant", "content": response1.content[0].text})
    conversation.append({"role": "user", "content": "Great! Can you explain what a list comprehension is?"})
    
    response2 = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=conversation
    )
    
    print(f"User: {conversation[2]['content']}")
    print(f"Claude: {response2.content[0].text}\n")
    
    # Example 3: Custom system prompt
    print("=" * 60)
    print("Example 3: Custom System Prompt")
    print("=" * 60)
    
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        system="You are a helpful coding assistant who explains concepts using simple analogies.",
        messages=[
            {"role": "user", "content": "What is recursion in programming?"}
        ]
    )
    
    print(f"Claude: {message.content[0].text}\n")
    
    print("=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("\nPlease make sure:")
        print("1. You have created a .env file with your ANTHROPIC_API_KEY")
        print("2. You have installed the required packages: pip install -r requirements.txt")
