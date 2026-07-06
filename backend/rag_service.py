from backend.retriever import retrieve
from backend.llm_service import generate_answer



def rag_pipeline(question: str):

    chunks = retrieve(question)

    answer = generate_answer(question, chunks)

    return answer