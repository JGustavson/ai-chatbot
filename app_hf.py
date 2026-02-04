#!/usr/bin/env python3
"""
Flask Web Server for Hugging Face Chatbot UI
"""

from flask import Flask, render_template, request, jsonify, session
from huggingface_hub import InferenceClient
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Configure Hugging Face API
HF_API_KEY = os.environ.get("HF_API_KEY")
if not HF_API_KEY:
    raise ValueError("Please set HF_API_KEY environment variable")

# Initialize Hugging Face client
client = InferenceClient(token=HF_API_KEY)

# Store chat sessions in memory
chat_sessions = {}

# Available models (you can change this)
# Popular free models on Hugging Face:
DEFAULT_MODEL = "meta-llama/Llama-3.2-3B-Instruct"
# Other options:
# "microsoft/Phi-3.5-mini-instruct"
# "mistralai/Mistral-7B-Instruct-v0.3"
# "Qwen/Qwen2.5-7B-Instruct"

def get_or_create_chat(session_id):
    """Get existing chat session or create a new one."""
    if session_id not in chat_sessions:
        chat_sessions[session_id] = []
    return chat_sessions[session_id]

@app.route('/')
def index():
    """Serve the chat interface."""
    if 'session_id' not in session:
        session['session_id'] = secrets.token_hex(16)
    return render_template('index_hf.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages."""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get or create chat session
        session_id = session.get('session_id')
        history = get_or_create_chat(session_id)
        
        # Add user message to history
        history.append({
            "role": "user",
            "content": user_message
        })
        
        # Get response from Hugging Face
        response_text = ""
        
        try:
            # Use chat completion with conversation history
            messages = history.copy()
            
            response = client.chat_completion(
                model=DEFAULT_MODEL,
                messages=messages,
                max_tokens=1000,
                temperature=0.7,
            )
            
            response_text = response.choices[0].message.content
            
            # Add assistant response to history
            history.append({
                "role": "assistant",
                "content": response_text
            })
            
            return jsonify({
                'response': response_text,
                'success': True,
                'model': DEFAULT_MODEL
            })
            
        except Exception as e:
            error_msg = str(e)
            print(f"Error: {error_msg}")
            
            # If rate limited, provide helpful message
            if "rate limit" in error_msg.lower() or "429" in error_msg:
                return jsonify({
                    'error': 'Rate limit reached. Please wait a moment and try again.',
                    'success': False
                }), 429
            
            return jsonify({
                'error': f'API Error: {error_msg}',
                'success': False
            }), 500
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/clear', methods=['POST'])
def clear_history():
    """Clear conversation history."""
    try:
        session_id = session.get('session_id')
        if session_id in chat_sessions:
            chat_sessions[session_id] = []
        
        return jsonify({
            'success': True,
            'message': 'Conversation cleared'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history."""
    try:
        session_id = session.get('session_id')
        history = chat_sessions.get(session_id, [])
        
        return jsonify({'history': history})
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'history': []
        }), 500

if __name__ == '__main__':
    print("=" * 60)
    print("Hugging Face Chatbot Web UI")
    print("=" * 60)
    print(f"Using model: {DEFAULT_MODEL}")
    print("Server starting at http://localhost:5000")
    print("Press Ctrl+C to stop")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
