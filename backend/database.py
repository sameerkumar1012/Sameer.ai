"""
Database wiring for the FAQ cache.

The cache is an optimisation, not a requirement: if DATABASE_URL is absent or
the server is unreachable, the app still answers every question through the
RAG pipeline. So nothing in this module may raise at import time.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from backend.config import DATABASE_URL
from backend.logger import logger

Base = declarative_base()

engine = None
SessionLocal = None

if DATABASE_URL:
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine
        )
    except Exception as exc:  # bad URL, missing driver, etc.
        logger.warning("Database unavailable, FAQ cache disabled: %s", exc)
        engine = None
        SessionLocal = None
else:
    logger.info("DATABASE_URL not set — running without the FAQ cache.")


def db_enabled() -> bool:
    return SessionLocal is not None
