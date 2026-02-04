#!/usr/bin/env python3
"""
Simple AI Chatbot using Hugging Face
Requires: pip install huggingface_hub
"""

import os
from huggingface_hub import InferenceClient

class HuggingFaceChatbot:
    def __init__(self, api_key=None, model=None):
        """Initialize the chatbot with your Hugging Face API key."""
        self.api_key = api_key or os.environ.get("HF_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key required. Set HF_API_KEY environment variable "
                "or pass api_key parameter."
            )
        
        # Initialize the client
        self.client = InferenceClient(token=self.api_key)
        
        # Set the model (you can change this)
        self.model = model or "meta-llama/Llama-3.2-3B-Instruct"
        # Other good free options:
        # "microsoft/Phi-3.5-mini-instruct"
        # "mistralai/Mistral-7B-Instruct-v0.3"
        # "Qwen/Qwen2.5-7B-Instruct"
        
        # Conversation history
        self.conversation_history = []
    
    def chat(self, user_message):
        """Send a message and get a response."""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # Get response from Hugging Face
            response = self.client.chat_completion(
                model=self.model,
                messages=self.conversation_history,
                max_tokens=1000,
                temperature=0.7,
            )
            
            # Extract assistant's response
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            error_msg = str(e)
            if "rate limit" in error_msg.lower() or "429" in error_msg:
                return "⚠️ Rate limit reached. Please wait a moment and try again."
            return f"Error: {error_msg}"
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history = []
        print("Conversation history cleared.")
    
    def run(self):
        """Run the interactive chatbot."""
        print("=" * 60)
        print("Hugging Face AI Chatbot")
        print("=" * 60)
        print(f"Model: {self.model}")
        print("Commands:")
        print("  - Type your message to chat")
        print("  - Type 'clear' to clear conversation history")
        print("  - Type 'quit' or 'exit' to end the conversation")
        print("=" * 60)
        print()
        
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for commands
                if user_input.lower() in ['quit', 'exit']:
                    print("\nGoodbye!")
                    break
                
                if user_input.lower() == 'clear':
                    self.clear_history()
                    continue
                
                # Get and display response
                print("\n🤗 AI: ", end="", flush=True)
                response = self.chat(user_input)
                print(response)
                print()
                
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"\nError: {e}")
                print("Please try again.\n")


def main():
    """Main function to run the chatbot."""
    try:
        # Initialize and run the chatbot
        chatbot = HuggingFaceChatbot()
        chatbot.run()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("\nTo use this chatbot, you need a Hugging Face API key.")
        print("Get one at: https://huggingface.co/settings/tokens")
        print("\nThen set it as an environment variable:")
        print("  export HF_API_KEY='your-api-key-here'")


if __name__ == "__main__":
    main()
