from backend.llm_service import generate_answer
from backend.retriever import retrieve


def rag_pipeline(question: str):
    """
    Returns (answer, chunks).

    The chunks come back alongside the answer so the caller can show which
    parts of the corpus were actually retrieved — useful for the web UI, and
    the quickest way to spot a bad retrieval.
    """

    chunks = retrieve(question)

    answer = generate_answer(question, chunks)

    return answer, chunks
