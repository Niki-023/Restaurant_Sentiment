"""
Content-based restaurant recommender: embed each restaurant's review text,
find nearest neighbors by cosine similarity.
"""

import numpy as np
from sklearn.neighbors import NearestNeighbors


def build_restaurant_embeddings(restaurant_reviews: dict[str, list[str]], model) -> dict[str, np.ndarray]:
    """
    restaurant_reviews: {business_id: [review_text, ...]}
    model: a SentenceTransformer instance
    Returns {business_id: averaged embedding vector}

    TODO: for each restaurant, embed all (or a sample of) its reviews and
    average the vectors into a single representation.
    """
    raise NotImplementedError


def fit_nearest_neighbors(embeddings: dict[str, np.ndarray], n_neighbors: int = 6) -> tuple[NearestNeighbors, list[str]]:
    """Fit a NearestNeighbors index over restaurant embeddings. Returns (model, business_id_order)."""
    ids = list(embeddings.keys())
    matrix = np.stack([embeddings[i] for i in ids])
    nn = NearestNeighbors(n_neighbors=n_neighbors, metric="cosine")
    nn.fit(matrix)
    return nn, ids


def get_similar_restaurants(business_id: str, nn_model: NearestNeighbors, ids: list[str], embeddings: dict[str, np.ndarray], top_k: int = 5) -> list[str]:
    """Returns top_k similar business_ids, excluding the input itself."""
    idx = ids.index(business_id)
    vector = embeddings[business_id].reshape(1, -1)
    distances, indices = nn_model.kneighbors(vector, n_neighbors=top_k + 1)
    similar = [ids[i] for i in indices[0] if ids[i] != business_id]
    return similar[:top_k]
