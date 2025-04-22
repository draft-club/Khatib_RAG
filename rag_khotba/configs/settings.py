# Configuration settings for the rag_khotba project

# Model and index paths
MODEL_PATH = "models/zephyr-7b-beta.Q4_K_M.gguf"
INDEX_PATH = "faiss_index/khotba.index"

# Audio settings
USE_TTS = True  # Toggle for text-to-speech functionality
TTS_SERVICE = "google"  # Specify the TTS service to use

# Data paths
DATA_PATH = "data/khotbas/"  # Path to the raw Khotba text data

# Other settings
MAX_CHUNKS = 1000  # Maximum number of chunks to retrieve
EMBEDDING_DIMENSION = 768  # Dimension of the embeddings used