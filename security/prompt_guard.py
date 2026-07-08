
import re

BLOCKED_PATTERNS = [

    r"ignore previous",

    r"ignore all",

    r"system prompt",

    r"developer prompt",

    r"repeat your instructions",

    r"show your prompt",

    r"reveal prompt",

    r"print prompt",

    r"pretend to",

    r"act as",

    r"jailbreak",

    r"dan mode",

    r"bypass",

    r"override",

    r"disable safety",

    r"api key",

    r"aws credentials",

    r"\.env",

    r"environment variables",

    r"secret key",

]

compiled = [re.compile(p, re.IGNORECASE) for p in BLOCKED_PATTERNS]


class PromptInjectionError(Exception):
    pass


def detect_prompt_injection(question: str):

    for pattern in compiled:

        if pattern.search(question):
            raise PromptInjectionError(
                "Potential prompt injection detected."
            )

    return True