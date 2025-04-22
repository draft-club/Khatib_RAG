from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name='sentence-transformers/arabic-sentence-transformer'):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, texts):
        return self.model.encode(texts, convert_to_tensor=True)

    def embed_single(self, text):
        return self.embed_text([text])[0]