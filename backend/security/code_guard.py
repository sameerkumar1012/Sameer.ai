
import re

MALICIOUS_KEYWORDS = [

    "malware",

    "virus",

    "keylogger",

    "reverse shell",

    "shellcode",

    "botnet",

    "ddos",

    "payload",

    "sql injection",

    "xss",

    "csrf exploit",

    "ransomware",

    "privilege escalation",

]

compiled = [
    re.compile(re.escape(word), re.IGNORECASE)
    for word in MALICIOUS_KEYWORDS
]


class UnsafeCodeRequest(Exception):
    pass


def detect_malicious_request(question: str):

    for pattern in compiled:

        if pattern.search(question):
            raise UnsafeCodeRequest(
                "Unsafe request detected."
            )

    return True