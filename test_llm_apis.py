
import os
import requests

from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_AI_API_KEY = os.getenv("GOOGLE_AI_API_KEY")
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434")


def test_openrouter():
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Say hello from OpenRouter!"}]
    }
    r = requests.post(url, headers=headers, json=data)
    print("OpenRouter:", r.status_code, r.json())

def test_groq():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    # Use latest recommended production model (Llama 3.3 70B Versatile)
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": "Say hello from Groq!"}]
    }
    r = requests.post(url, headers=headers, json=data)
    print("Groq:", r.status_code, r.json())

def test_google_ai():
    # Use latest recommended Gemini model (Gemini 3.1 Pro Preview)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent?key={GOOGLE_AI_API_KEY}"
    data = {
        "contents": [{"parts": [{"text": "Say hello from Google Gemini!"}]}]
    }
    r = requests.post(url, json=data)
    print("Google AI Gemini:", r.status_code, r.json())


def test_ollama(model_name):
    url = f"{OLLAMA_API_URL}/api/chat"
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": f"Say hello from Ollama model {model_name}!"}]
    }
    try:
        r = requests.post(url, json=data, stream=True)
        # Ollama may return streaming JSON (one object per line)
        lines = r.text.strip().splitlines()
        for line in lines:
            try:
                resp = line.strip()
                if resp:
                    import json
                    obj = json.loads(resp)
                    if 'message' in obj and 'content' in obj['message']:
                        print(f"Ollama ({model_name}):", obj['message']['content'])
            except Exception as e:
                print(f"Ollama ({model_name}): JSON parse error -", e)
    except Exception as e:
        print(f"Ollama ({model_name}): Error -", e)

if __name__ == "__main__":
    print("Testing OpenRouter...")
    test_openrouter()
    print("Testing Groq...")
    test_groq()
    print("Testing Google AI Gemini...")
    test_google_ai()
    ollama_models = [
        "gpt-3.6-turbo:latest",
        "deepseek-coder:latest",
        "qwen3:latest",
        "qwen3-4b:latest",
        "qwen3:4b"
    ]
    for model in ollama_models:
        print(f"Testing Ollama ({model})...")
        test_ollama(model)
