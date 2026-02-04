# 🤗 Hugging Face AI Chatbot - 100% FREE!

A beautiful web interface and command-line chatbot powered by Hugging Face's free AI models. **No credit card required!**

## Why Hugging Face?

✅ **100% FREE** - 1,000 API requests per month  
✅ **No credit card required** - Just create an account  
✅ **Open-source models** - Choose from hundreds of models  
✅ **Fast and reliable** - Production-ready infrastructure  
✅ **Privacy-friendly** - Your data isn't used for training  

## Quick Start

### 1. Get Your FREE API Key

1. Go to https://huggingface.co/join to create a free account
2. Go to https://huggingface.co/settings/tokens
3. Click "New token" → Create a token with "read" access
4. Copy your token

**No credit card required!** ✨

### 2. Install Dependencies

```bash
pip install -r hf_requirements.txt
```

This installs:
- `flask` - Web framework
- `huggingface_hub` - Hugging Face API client

### 3. Set Your API Key

**Linux/Mac:**
```bash
export HF_API_KEY='your-api-key-here'
```

**Windows (Command Prompt):**
```cmd
set HF_API_KEY=your-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:HF_API_KEY='your-api-key-here'
```

### 4. Run the Application

**Web Interface:**
```bash
python app_hf.py
```
Then open `http://localhost:5000` in your browser

**Command Line:**
```bash
python hf_chatbot.py
```

## Available Models

The chatbot uses **Llama 3.2 3B** by default (fast and capable). You can switch to other free models:

### Popular Free Models:

**Fast & Efficient:**
- `meta-llama/Llama-3.2-3B-Instruct` (Default - Great balance)
- `microsoft/Phi-3.5-mini-instruct` (Very fast, compact)
- `mistralai/Mistral-7B-Instruct-v0.3` (Popular, reliable)

**More Capable:**
- `Qwen/Qwen2.5-7B-Instruct` (Excellent quality)
- `meta-llama/Llama-3.1-8B-Instruct` (Strong reasoning)

**Specialized:**
- `codellama/CodeLlama-13b-Instruct-hf` (Great for coding)
- `HuggingFaceH4/zephyr-7b-beta` (Conversational)

### How to Change Models

**In `app_hf.py`:**
```python
DEFAULT_MODEL = "microsoft/Phi-3.5-mini-instruct"  # Change this line
```

**In `hf_chatbot.py`:**
```python
self.model = "Qwen/Qwen2.5-7B-Instruct"  # Change this line
```

Or pass it when creating the chatbot:
```python
chatbot = HuggingFaceChatbot(model="mistralai/Mistral-7B-Instruct-v0.3")
```

## Project Structure

```
.
├── app_hf.py                   # Flask web server
├── hf_chatbot.py              # Command-line chatbot
├── hf_requirements.txt        # Dependencies
├── templates/
│   └── index_hf.html          # Web interface HTML
└── static/
    ├── css/
    │   └── style.css          # Styles
    └── js/
        └── app.js             # Frontend JavaScript
```

## Features

### Web Interface
- 🎨 Beautiful dark theme with Hugging Face branding
- 💬 Real-time chat with conversation history
- ⚡ Fast responses
- 📱 Responsive mobile design
- 🔄 Clear conversation button
- ⌨️ Keyboard shortcuts (Enter to send)

### Command Line
- 💻 Simple terminal interface
- 📝 Conversation history
- 🔄 Clear command
- ⚡ Fast and lightweight

## Free Tier Limits

Hugging Face Inference API (Free):
- **1,000 requests per month**
- **Resets monthly**
- **No credit card required**

If you need more:
- **Pro Account**: $9/month for 100x more requests
- **Self-hosting**: Run models locally for unlimited use

## Usage Examples

### Web Chat
Just type your message and press Enter!

### Command Line
```bash
$ python hf_chatbot.py
You: Hello! How are you?
🤗 AI: I'm doing well, thank you! How can I help you today?
```

### Programmatic Use
```python
from hf_chatbot import HuggingFaceChatbot

# Initialize
bot = HuggingFaceChatbot(api_key="your-key")

# Chat
response = bot.chat("Tell me a fun fact about Python")
print(response)

# Continue conversation (history maintained)
response = bot.chat("Tell me more!")
print(response)

# Clear history
bot.clear_history()
```

## Customization

### Change Temperature (Creativity)
In `app_hf.py` or `hf_chatbot.py`:
```python
response = client.chat_completion(
    model=self.model,
    messages=messages,
    max_tokens=1000,
    temperature=0.9,  # Higher = more creative (0.0 - 1.0)
)
```

### Change Max Tokens (Response Length)
```python
max_tokens=2000,  # Longer responses
```

### Add System Message
```python
messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    *self.conversation_history
]
```

## Troubleshooting

### "API key required" error
Make sure you've set the `HF_API_KEY` environment variable and restarted your terminal.

### "Rate limit exceeded"
You've used your 1,000 free requests for the month. Wait until next month or upgrade to Pro.

### "Model not found"
Some models require accepting a license on Hugging Face. Visit the model page and accept the terms.

### Slow responses
Try a smaller/faster model like `microsoft/Phi-3.5-mini-instruct`

## Comparison: Hugging Face vs Others

| Feature | Hugging Face | Google Gemini | OpenAI |
|---------|-------------|---------------|---------|
| **Free Tier** | ✅ 1,000/month | ✅ 1,500/day | ❌ Requires $5 |
| **No CC Required** | ✅ Yes | ✅ Yes | ❌ No |
| **Model Choice** | ✅ 100+ models | ❌ Fixed | ❌ Fixed |
| **Open Source** | ✅ Yes | ❌ No | ❌ No |
| **Privacy** | ✅ Excellent | ⚠️ Good | ⚠️ Limited |

## Advanced: Self-Hosting Models

Want unlimited free usage? Run models locally:

```bash
# Install transformers
pip install transformers torch

# Download and run a model
from transformers import pipeline

chatbot = pipeline("text-generation", model="microsoft/Phi-3.5-mini-instruct")
response = chatbot("Hello, how are you?")
```

Requires:
- Good GPU (recommended)
- Or use CPU (slower but works)

## Get Help

- **Hugging Face Docs**: https://huggingface.co/docs
- **API Docs**: https://huggingface.co/docs/api-inference
- **Community**: https://discuss.huggingface.co/

## Tips for Best Results

1. **Be specific** - Clear questions get better answers
2. **Use context** - The chatbot remembers conversation history
3. **Try different models** - Each has strengths
4. **Experiment with temperature** - Adjust creativity vs accuracy
5. **Keep requests reasonable** - Stay within rate limits

## Upgrading

Need more requests?

**Hugging Face Pro** ($9/month):
- 100,000+ requests/month
- Faster inference
- Access to exclusive models
- Priority support

**Or self-host for free!**

## License

Free to use and modify for personal and commercial projects.

Enjoy your FREE AI chatbot! 🤗✨
