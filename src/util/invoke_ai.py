import requests

def invoke_ai(system_message: str, user_message: str) -> str:
    """
    Invokes the locally hosted llama3 model via Ollama API.
    This version uses ONLY Ollama. OpenAI is completely removed.
    """
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3",  # Uses locally pulled `llama3`
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["message"]["content"].strip()
    except Exception as e:
        return f"[Ollama llama3 Error] {str(e)}"