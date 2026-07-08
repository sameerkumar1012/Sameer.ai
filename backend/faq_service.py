from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.config import FAQ_THRESHOLD
from backend.utils import normalize


def search_faq(db: Session, question: str):

    normalized = normalize(question)

    # ----------------------------------------------------
    # 1. Exact Match (Fastest)
    # ----------------------------------------------------

    exact_query = text("""
        SELECT
            question,
            answer
        FROM faq
        WHERE normalized_question = :question
        LIMIT 1
    """)

    exact = db.execute(
        exact_query,
        {"question": normalized}
    ).fetchone()

    if exact:

        print("\n" + "=" * 70)
        print("Question        :", question)
        print("Normalized      :", normalized)
        print("FAQ Match Type  : EXACT")
        print("Matched FAQ     :", exact.question)
        print("=" * 70)

        return exact

    # ----------------------------------------------------
    # 2. Trigram Similarity Search
    # ----------------------------------------------------

    similarity_query = text("""
        SELECT
            question,
            answer,
            normalized_question,
            similarity(normalized_question, :question) AS score
        FROM faq
        WHERE similarity(normalized_question, :question) >= :threshold
        ORDER BY score DESC
        LIMIT 1
    """)

    result = db.execute(
        similarity_query,
        {
            "question": normalized,
            "threshold": FAQ_THRESHOLD
        }
    ).fetchone()

    print("\n" + "=" * 70)
    print("Question        :", question)
    print("Normalized      :", normalized)

    if result:
        print("FAQ Match Type  : TRIGRAM")
        print("Matched FAQ     :", result.question)
        print("Normalized FAQ  :", result.normalized_question)
        print("Similarity      :", round(result.score, 3))
    else:
        print("FAQ Match Type  : NONE")
        print("Action          : Falling back to RAG")

    print("=" * 70)

    return result