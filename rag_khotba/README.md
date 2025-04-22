# rag_khotba Project

## Overview
The `rag_khotba` project is a Streamlit application designed for processing and retrieving Arabic sermons (Khotbas). It utilizes various components such as embeddings, retrieval mechanisms, and text-to-speech functionality to provide an interactive user experience.

## Directory Structure
```
rag_khotba/
├── app/
│   └── streamlit_app.py                  # Entry point: Streamlit interface
├── configs/
│   └── settings.py                       # Config variables (e.g., model path, index path, audio toggles)
├── data/
│   └── khotbas/                          # Raw Khotba text data (Arabic sermons)
├── embeddings/
│   ├── embedder.py                       # SentenceTransformer Arabic embedding
│   └── index_builder.py                  # Chunking + FAISS vector index creation
├── retrieval/
│   └── retriever.py                      # Load FAISS index + retrieve relevant chunks
├── generation/
│   └── generator.py                      # Prompt creation + LLM response
├── audio/
│   ├── tts_google.py                     # Arabic TTS using Google Cloud API
│   └── __init__.py
├── faiss_index/
│   ├── khotba.index                      # Saved FAISS vector index
│   └── doc_ids.pkl                       # Metadata for chunks
├── models/
│   └── zephyr-7b-beta.Q4_K_M.gguf        # Quantized GGUF model (locally downloaded)
├── requirements.txt                      # All needed Python dependencies
└── README.md                             # Project setup + usage
```

## Setup Instructions
1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd rag_khotba
   ```

2. **Install Dependencies**
   Ensure you have Python 3.7 or higher installed. Then, install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Settings**
   Modify the `configs/settings.py` file to set the appropriate paths for your model and index files.

4. **Run the Application**
   Start the Streamlit application by running:
   ```
   streamlit run app/streamlit_app.py
   ```

## Usage
- The application allows users to input queries related to Khotbas and retrieves relevant sermons.
- Users can listen to the sermons using the text-to-speech functionality.
- The application is designed to be user-friendly and interactive.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.