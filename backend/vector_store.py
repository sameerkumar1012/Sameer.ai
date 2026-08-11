"""
Builds the FAISS index from the markdown knowledge base.

Run after editing anything in `knowledge/`:

    python -m backend.vector_store
"""

import pickle

import faiss
import numpy as np

from backend.chunker import (
    load_markdown_files,
    chunk_markdown
)

from backend.config import KNOWLEDGE_DIR, METADATA_FILE, VECTOR_INDEX
from backend.embeddings import get_embedding

# Gives each chunk a topic word its own body often lacks. Without this, a
# chunk like "Databases -> - MySQL" carries no signal about what it is.
TOPICS = {
    "skills.md": "Skills and technologies",
    "projects.md": "Project",
    "experience.md": "Work experience",
    "education.md": "Education",
    "profile.md": "Profile and contact details",
}


def build_embedding_text(filename: str, title: str, content: str) -> str:
    """
    Text actually sent to the embedding model.

    The heading matters as much as the body — "Cloud & Data Warehousing"
    is the only place the word "cloud" appears in that chunk, so embedding
    the body alone makes it unretrievable by an obvious question.
    """

    topic = TOPICS.get(filename, filename.replace(".md", ""))

    return f"{topic}: {title}\n\n{content}"


def build_vector_store():

    embeddings = []

    metadata = []

    docs = load_markdown_files(KNOWLEDGE_DIR)

    for doc in docs:

        chunks = chunk_markdown(doc["content"])

        for chunk in chunks:

            if not chunk["content"].strip():
                continue

            text = build_embedding_text(
                doc["filename"],
                chunk["title"],
                chunk["content"],
            )

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

    faiss.write_index(index, str(VECTOR_INDEX))

    with open(METADATA_FILE, "wb") as f:

        pickle.dump(metadata, f)

    print("=" * 50)
    print("Vector Store Built Successfully")
    print(f"Total Chunks : {len(metadata)}")


if __name__ == "__main__":

    build_vector_store()
