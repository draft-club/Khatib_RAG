from typing import List
import faiss
import numpy as np
import pickle
from configs.settings import INDEX_PATH, DOC_IDS_PATH

class Retriever:
    def __init__(self):
        self.index = self.load_index()
        self.doc_ids = self.load_doc_ids()

    def load_index(self):
        index = faiss.read_index(INDEX_PATH)
        return index

    def load_doc_ids(self):
        with open(DOC_IDS_PATH, 'rb') as f:
            doc_ids = pickle.load(f)
        return doc_ids

    def retrieve(self, query_embedding: np.ndarray, top_k: int = 5) -> List[str]:
        distances, indices = self.index.search(query_embedding, top_k)
        retrieved_docs = [self.doc_ids[i] for i in indices[0]]
        return retrieved_docs, distances[0]