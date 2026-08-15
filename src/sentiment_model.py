"""
Sentiment classification: baseline (TF-IDF + LogisticRegression) and,
optionally, a fine-tuned transformer. Trained in notebooks/, saved to
models/, loaded here for reuse in the app.
"""

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def build_baseline_pipeline() -> Pipeline:
    """
    TF-IDF + Logistic Regression baseline. Train this FIRST before anything
    fancier — it's your reference point for "is the complex model worth it?"
    """
    return Pipeline([
        ("tfidf", TfidfVectorizer(max_features=20_000, ngram_range=(1, 2), stop_words="english")),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced")),
    ])


def save_model(model, path: str) -> None:
    joblib.dump(model, path)


def load_model(path: str):
    return joblib.load(path)


def predict_sentiment(model, texts: list[str]) -> list[str]:
    """Returns predicted labels for a list of review texts."""
    return model.predict(texts).tolist()
