from typing import List
import faiss
import numpy as np

class IndexBuilder:
    def __init__(self, embeddings: List[np.ndarray], dimension: int):
        self.embeddings = np.array(embeddings).astype('float32')
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(self.dimension)

    def build_index(self):
        self.index.add(self.embeddings)

    def save_index(self, index_path: str):
        faiss.write_index(self.index, index_path)

    def load_index(self, index_path: str):
        self.index = faiss.read_index(index_path)