import requests

OLLAMA_URL = "http://localhost:11434"

def generate_response(prompt, model="llama3"):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": model, "prompt": prompt}
    )
    response.raise_for_status()
    return response.json()["response"].strip()

def embed_text(text, model="nomic-embed-text"):
    response = requests.post(
        f"{OLLAMA_URL}/api/embed",
        json={"model": model, "input": text}
    )
    response.raise_for_status()
    return response.json()["embedding"]