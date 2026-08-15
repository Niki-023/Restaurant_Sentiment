"""
Keyword-based aspect extraction (v1). For each review, figure out which
sentences mention which aspect (food/service/ambiance/value), then run
sentiment on just those sentences.

v2 idea: swap this out for a pretrained aspect-based sentiment model
once the basic pipeline works end to end.
"""

ASPECT_KEYWORDS = {
    "food": ["food", "dish", "meal", "taste", "flavor", "menu", "portion"],
    "service": ["service", "waiter", "waitress", "staff", "server", "host"],
    "ambiance": ["ambiance", "atmosphere", "decor", "music", "noise", "seating"],
    "value": ["price", "value", "worth", "expensive", "cheap", "cost"],
}


def split_sentences(text: str) -> list[str]:
    """Naive sentence splitter — swap for nltk.sent_tokenize if you want more accuracy."""
    import re
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def extract_aspect_sentences(review_text: str) -> dict[str, list[str]]:
    """
    Returns {aspect: [matching sentences]} for a single review.
    A sentence can match multiple aspects.
    """
    sentences = split_sentences(review_text)
    result = {aspect: [] for aspect in ASPECT_KEYWORDS}
    for sentence in sentences:
        lowered = sentence.lower()
        for aspect, keywords in ASPECT_KEYWORDS.items():
            if any(kw in lowered for kw in keywords):
                result[aspect].append(sentence)
    return result
