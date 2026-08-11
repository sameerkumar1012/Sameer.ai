"""
FAISS retrieval over the resume corpus.

The index is loaded lazily and cached, so importing this module never touches
the filesystem — that keeps `uvicorn` startup and `/healthz` working even if
the artefacts are missing, and it stops import order from mattering.
"""

import pickle

import faiss
import numpy as np

from backend.config import METADATA_FILE, TOP_K, VECTOR_INDEX
from backend.embeddings import get_embedding

_index = None
_metadata = None


def _load():
    global _index, _metadata

    if _index is None or _metadata is None:
        if not VECTOR_INDEX.exists() or not METADATA_FILE.exists():
            raise FileNotFoundError(
                f"Vector store missing. Expected {VECTOR_INDEX} and "
                f"{METADATA_FILE}. Run `python -m backend.vector_store`."
            )

        _index = faiss.read_index(str(VECTOR_INDEX))

        with open(METADATA_FILE, "rb") as f:
            _metadata = pickle.load(f)

    return _index, _metadata


def retrieve(question: str, top_k: int = TOP_K):
    index, metadata = _load()

    question_embedding = np.array(
        [get_embedding(question)],
        dtype="float32"
    )

    distances, indices = index.search(question_embedding, top_k)

    results = []

    for idx in indices[0]:

        # FAISS returns -1 when it has fewer vectors than top_k.
        if idx < 0 or idx >= len(metadata):
            continue

        results.append(metadata[idx])

    return results


## test
if __name__ == "__main__":

    chunks = retrieve(
        "What cloud technologies does Sameer know?"
    )

    for chunk in chunks:

        print("=" * 50)

        print(chunk["source"])

        print(chunk["title"])

        print(chunk["content"])
