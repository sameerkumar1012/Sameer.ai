from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.utils import normalize


def search_faq(db: Session, question: str):

    normalized = normalize(question)

    query = text("""
        SELECT
            question,
            answer,
            similarity(normalized_question, :question) AS score
        FROM faq
        ORDER BY score DESC
        LIMIT 1
    """)

    result = db.execute(
        query,
        {"question": normalized}
    ).fetchone()

    if result is None:
        return None

    if result.score >= 0.65:
        return result

    return None