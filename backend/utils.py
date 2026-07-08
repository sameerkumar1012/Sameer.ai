import re

STOP_WORDS = {
    "what", "are", "is", "does", "do", "did",
    "tell", "me", "about", "the",
    "a", "an", "can", "you",
    "please", "have", "has", "know", "knows",
    "your", "during", "with", "of", "to", "in",
    "on", "for", "and"
}

SYNONYMS = {

    # ---------- Person ----------
    "his": "sameer",
    "him": "sameer",
    "he": "sameer",
    "candidate": "sameer",

    # ---------- Projects ----------
    "project": "projects",
    "portfolio": "projects",

    # ---------- Skills ----------
    "skill": "skills",
    "skills": "skills",

    # ---------- Technology ----------
    "tech": "technology",
    "technologies": "technology",
    "technology": "technology",

    # ---------- AI ----------
    "llms": "llm",
    "rags": "rag",

    # ---------- Education ----------
    "college": "education",
    "university": "education",
    "degree": "education",

    # ---------- Experience ----------
    "internship": "experience",
    "intern": "experience",
    "work": "experience",

    # ---------- Resume ----------
    "background": "profile",
    "introduction": "profile",
    "introduce": "profile",
    "who": "profile"
}


def normalize(text: str):

    text = text.lower()

    text = re.sub(r"[^a-z0-9 ]", " ", text)

    words = []

    for word in text.split():

        if word in STOP_WORDS:
            continue

        words.append(
            SYNONYMS.get(word, word)
        )

    return " ".join(words)