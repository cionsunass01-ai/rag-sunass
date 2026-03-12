# rag_sunass/embeddings.py

from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings


MODEL_NAME = "BAAI/bge-m3"


class BGEM3Embeddings(Embeddings):
    """Wrapper LangChain para BGE-M3 vía sentence-transformers."""

    def __init__(self, model_name: str = MODEL_NAME, device: str = "cpu"):
        self.model = SentenceTransformer(model_name, device=device)
        self.device = device

    def _encode(self, textos: List[str]) -> np.ndarray:
        vecs = self.model.encode(
            textos,
            normalize_embeddings=True,
            batch_size=8,
            show_progress_bar=False,
        )
        return np.array(vecs, dtype=np.float32)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._encode(texts).tolist()

    def embed_query(self, text: str) -> List[float]:
        return self._encode([text])[0].tolist()
