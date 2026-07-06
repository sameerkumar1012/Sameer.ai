import faiss
import pickle
import numpy as np
from backend.config import TOP_K


from backend.embeddings import get_embedding


index = faiss.read_index("vector.index")

with open("metadata.pkl", "rb") as f:
    metadata = pickle.load(f)


def retrieve(question: str, top_k: int = TOP_K):
    question_embedding = np.array(
        [get_embedding(question)],
        dtype="float32"
    )

    distances, indices = index.search(question_embedding, top_k)

    results = []

    for idx in indices[0]:

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