from pathlib import Path


def load_markdown_files(folder: str):

    folder = Path(folder)

    documents = []

    for file in folder.glob("*.md"):

        with open(file, "r", encoding="utf-8") as f:

            documents.append({
                "filename": file.name,
                "content": f.read()
            })

    return documents

import re


def chunk_markdown(content):

    chunks = []

    current_title = None
    current_content = []

    for line in content.splitlines():

        if line.startswith("## "):

            if current_title:

                chunks.append({
                    "title": current_title,
                    "content": "\n".join(current_content).strip()
                })

            current_title = line.replace("## ", "").strip()
            current_content = []

        elif line.startswith("# "):
            continue

        else:
            current_content.append(line)

    if current_title:

        chunks.append({
            "title": current_title,
            "content": "\n".join(current_content).strip()
        })

    return chunks

## Test
if __name__ == "__main__":

    docs = load_markdown_files("knowledge")

    for doc in docs:

        print("\n" + "=" * 60)
        print(doc["filename"])

        chunks = chunk_markdown(doc["content"])

        print(f"Total Chunks: {len(chunks)}")

        for i, chunk in enumerate(chunks, start=1):

            print("\n" + "-" * 40)
            print(f"Chunk {i}")
            print(f"Title : {chunk['title']}")
            print()
            print(chunk["content"])