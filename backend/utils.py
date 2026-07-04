import re

STOP_WORDS = {
    "what", "are", "is", "does", "do",
    "tell", "me", "about", "the",
    "a", "an", "can", "you",
    "please", "have", "has", "know",
    "knows"
}

SYNONYMS = {
    "technology": "skills",
    "technologies": "skills",
    "tech": "skills",
    "stack": "skills",

    "his": "sameer",
    "him": "sameer",
    "he": "sameer",

    "project": "projects",
    "projects": "projects",

    "background": "profile",
    "experience": "profile"
}


def normalize(text: str):

    text = text.lower()

    text = re.sub(r"[^a-z0-9 ]", "", text)

    words = []

    for word in text.split():

        if word in STOP_WORDS:
            continue

        word = SYNONYMS.get(word, word)

        words.append(word)

    return " ".join(words)