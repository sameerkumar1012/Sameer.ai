from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from backend.database import Base


class FAQ(Base):
    __tablename__ = "faq"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(Text, nullable=False)

    normalized_question = Column(Text, nullable=False)

    answer = Column(Text, nullable=False)

    usage_count = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())