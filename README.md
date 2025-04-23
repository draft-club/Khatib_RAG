# RAG Khotba: Arabic Sermon Retrieval & Generation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**RAG Khotba** is a sophisticated Retrieval-Augmented Generation (RAG) system tailored for processing, indexing, and interacting with Arabic sermons (Khotbas). It leverages state-of-the-art NLP techniques to provide an intuitive Streamlit interface for querying sermon content, retrieving relevant passages using FAISS-accelerated vector search, generating coherent responses with a powerful local language model, and optionally delivering results via Arabic text-to-speech.

---

## ✨ Features

*   **🖥️ Interactive Streamlit UI:** User-friendly web interface for seamless interaction.
*   **🇸🇦 Arabic Embeddings:** High-quality sentence embeddings specialized for Arabic using SentenceTransformer.
*   **⚡ Fast Retrieval:** Efficient semantic search powered by FAISS vector indexing.
*   **🧠 Local LLM Generation:** On-device response generation using a quantized GGUF model (Zephyr 7B Beta).
*   **🗣️ Arabic Text-to-Speech:** Optional audio output of generated responses via Google Cloud TTS.
*   **🔧 Configurable:** Easily adjust settings like model paths, index locations, and feature toggles.

---

