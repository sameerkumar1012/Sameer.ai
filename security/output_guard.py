import re

SENSITIVE_PATTERNS = [

    r"AKIA[0-9A-Z]{16}",

    r"-----BEGIN PRIVATE KEY-----",

    r"password\s*=",

    r"SECRET_KEY",

    r"AWS_SECRET_ACCESS_KEY",

    r"Traceback \(most recent call last\)",

    r"sqlalchemy",

    r"File \".*\", line \d+",

]

compiled = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in SENSITIVE_PATTERNS
]


SAFE_MESSAGE = (
    "⚠️ The generated response was blocked because it contained "
    "sensitive information."
)


def sanitize_output(text: str):

    for pattern in compiled:

        if pattern.search(text):
            return SAFE_MESSAGE

    return text