import faiss
import pickle
import numpy as np

from backend.chunker import (
    load_markdown_files,
    chunk_markdown
)

from backend.embeddings import get_embedding


def build_vector_store():

    embeddings = []

    metadata = []

    docs = load_markdown_files("knowledge")

    for doc in docs:

        chunks = chunk_markdown(doc["content"])

        for chunk in chunks:

            text = chunk["content"]

            vector = get_embedding(text)

            embeddings.append(vector)

            metadata.append({

                "source": doc["filename"],

                "title": chunk["title"],

                "content": chunk["content"]

            })

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, "vector.index")

    with open("metadata.pkl", "wb") as f:

        pickle.dump(metadata, f)

    print("=" * 50)
    print("Vector Store Built Successfully")
    print(f"Total Chunks : {len(metadata)}")


if __name__ == "__main__":

    build_vector_store()