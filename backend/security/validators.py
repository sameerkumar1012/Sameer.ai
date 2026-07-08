import re
import unicodedata

MAX_QUESTION_LENGTH = 500


class ValidationError(Exception):
    pass


def validate_question(question: str) -> str:
    """
    Validate incoming user question.
    """

    if not question:
        raise ValidationError("Question cannot be empty.")

    question = unicodedata.normalize("NFKC", question)

    question = question.strip()

    if not question:
        raise ValidationError("Question cannot be empty.")

    if len(question) > MAX_QUESTION_LENGTH:
        raise ValidationError(
            f"Question exceeds {MAX_QUESTION_LENGTH} characters."
        )

    # Remove repeated spaces
    question = re.sub(r"\s+", " ", question)

    return question