"""
Text cleaning and dataset preparation utilities.
Fill these in during Phase 2 (EDA) and reuse them in later notebooks/app.
"""

import re
import pandas as pd


def load_filtered_reviews(review_path: str, business_ids: set, chunksize: int = 100_000) -> pd.DataFrame:
    """
    Stream yelp_academic_dataset_review.json and keep only reviews for the
    given business_ids. Returns a DataFrame with at least:
    ['business_id', 'text', 'stars', 'date'].

    TODO: implement with pd.read_json(review_path, lines=True, chunksize=chunksize)
    """
    raise NotImplementedError


def clean_text(text: str) -> str:
    """
    Basic cleaning: lowercase, strip extra whitespace, remove weird characters.
    Keep punctuation for now — sentence-level aspect extraction may need it.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    return text


def rating_to_sentiment_label(stars: float) -> str:
    """
    Convert a 1-5 star rating into a sentiment label.
    1-2 stars -> 'negative', 3 -> 'neutral', 4-5 -> 'positive'
    """
    if stars <= 2:
        return "negative"
    elif stars == 3:
        return "neutral"
    else:
        return "positive"
