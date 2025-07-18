# 🧠 Simple RAG Pipeline (Fully Local with Ollama + LLaMA3)

This project is a beginner-friendly, end-to-end implementation of a **Retrieval-Augmented Generation (RAG)** pipeline, running fully **locally** using [Ollama](https://ollama.com/) and [LLaMA3](https://ollama.com/library/llama3). It demonstrates how to ingest documents, embed and store them, search for relevant content, generate answers, and evaluate accuracy—all through a clean and modular CLI.

![RAG Image](./rag-design-basic.png)

---

## 🚀 Features

- ✅ Fully Local LLM with **Ollama + LLaMA3**
- 📄 Index PDFs or plain text documents using custom or Docling-based indexers
- 🔍 Embed text using **nomic-embed-text** (also via Ollama)
- 🧠 Vector search using **LanceDB**
- 🧵 Modular components for indexing, retrieval, generation, and evaluation
- 📊 CLI commands for adding, querying, and evaluating

---

## 🧱 Architecture

The pipeline is coordinated by `src/rag_pipeline.py` and includes:

- **Datastore:** Stores and retrieves vector embeddings via **LanceDB**
- **Indexer:** Splits and embeds documents using **nomic-embed-text** via Ollama
- **Retriever:** Performs similarity search and optional reranking
- **Response Generator:** Uses **LLaMA3** locally through Ollama
- **Evaluator:** Compares generated answers to expected ones from eval sets

Each component has a base class (`interface/`) so it can be swapped or extended easily.

---

## ⚙️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/sathvik6198/simple-rag-pipeline.git
cd simple-rag-pipeline
```

### 2. Set Up Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Ensure `numpy` version is `<2.0` due to compatibility with LanceDB.

---

## 🔧 Ollama Setup

Install Ollama from: https://ollama.com/download  
Then pull the required models:

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

---

## 📁 Folder Structure

```bash
.
├── main.py                  # CLI entry point
├── src/
│   ├── rag_pipeline.py      # Main RAG orchestrator
│   ├── impl/                # Implementation of pipeline steps
│   ├── util/                # Ollama client, embedding utilities
│   └── interface/           # Base interfaces for each component
├── sample_data/
│   ├── source/              # Add your PDFs or text here
│   └── eval/                # Evaluation question/answer pairs
```

---

## 🧪 CLI Usage

### Reset Vector Store

```bash
python main.py reset
```

### Index Documents

```bash
python main.py add -p "sample_data/source/"
```

### Query the System

```bash
python main.py query "What is the opening year of The Lagoon Breeze Hotel?"
```

### Evaluate with JSON File

```bash
python main.py evaluate -f "sample_data/eval/sample_questions.json"
```

---

## ✅ Requirements

```txt
pydantic>=2.0.0
lancedb==0.22.0
docling==2.31.0
cohere==5.15.0  # Optional – used for reranking (can be removed)
```

---

## 🙏 Acknowledgements

This project is inspired by [**pixegami/simple-rag-pipeline**](https://github.com/pixegami/simple-rag-pipeline), which provides a clean and extensible foundation for RAG.

My version includes:

- 🔒 **Full local inference** using **Ollama + LLaMA3**
- 🧠 Swapped embedding model to **nomic-embed-text** via Ollama
- 🧹 Removed OpenAI dependency
- ⚙️ Modular enhancements for easier local experimentation
