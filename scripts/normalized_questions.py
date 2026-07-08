
from sqlalchemy import text
from backend.database import SessionLocal
from backend.utils import normalize

db = SessionLocal()

rows = db.execute(
    text("SELECT id, question FROM faq")
).fetchall()

for row in rows:

    db.execute(
        text("""
            UPDATE faq
            SET normalized_question=:normalized
            WHERE id=:id
        """),
        {
            "normalized": normalize(row.question),
            "id": row.id
        }
    )

db.commit()

print("Updated all normalized questions.")