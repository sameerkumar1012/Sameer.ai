from backend.database import SessionLocal


def get_db():
    """
    Yields a session, or None when the FAQ cache is disabled.

    Callers must handle None — see `faq_lookup` in app.py.
    """

    if SessionLocal is None:
        yield None
        return

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
