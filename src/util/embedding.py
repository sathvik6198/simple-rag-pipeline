import requests

OLLAMA_URL = "http://localhost:11434"
OLLAMA_EMBED_MODEL = "nomic-embed-text"

def embed_text(text: str) -> list:
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/embed",
            json={"model": OLLAMA_EMBED_MODEL, "input": text}
        )
        response.raise_for_status()
        json_data = response.json()
        print("🔍 Ollama embed response: json data")  # DEBUG

        # Try 'embedding' or 'embeddings'
        if "embedding" in json_data:
            return json_data["embedding"]
        elif "embeddings" in json_data:
            return json_data["embeddings"][0]
        else:
            raise ValueError("No embedding or embeddings key in response")

    except Exception as e:
        raise RuntimeError(f"Ollama embedding failed: {e}")