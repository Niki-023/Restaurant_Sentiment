"""
Restaurant Review Sentiment & Recommender — Streamlit app.

This is a SKELETON. Build the model/pipeline in notebooks + src/ first
(Phases 2-6), then come back and wire it in here (Phase 7).
"""

import streamlit as st

st.set_page_config(page_title="Restaurant Review Analyzer", layout="wide")

st.title("🍽️ Restaurant Review Analyzer")
st.caption("Sentiment breakdown + similar-restaurant recommendations, powered by review text.")

# --- TODO Phase 7: load cached model/data ---
# @st.cache_resource
# def load_artifacts():
#     model = load_model("models/sentiment_model.joblib")
#     restaurants_df = pd.read_parquet("data/processed/restaurants.parquet")
#     embeddings = joblib.load("models/restaurant_embeddings.joblib")
#     return model, restaurants_df, embeddings

# --- Search / select restaurant ---
st.subheader("Search a restaurant")
# TODO: st.selectbox or st.text_input + search over restaurants_df["name"]

# --- Results section (placeholder layout) ---
col1, col2 = st.columns([1, 1])
with col1:
    st.subheader("Sentiment overview")
    # TODO: overall sentiment badge, star rating, review count

    st.subheader("Aspect breakdown")
    # TODO: bar/radar chart of food/service/ambiance/value sentiment

with col2:
    st.subheader("What people love")
    # TODO: top positive themes

    st.subheader("What people complain about")
    # TODO: top negative themes

st.subheader("Similar restaurants")
# TODO: card grid using recommend.get_similar_restaurants()

st.divider()
st.subheader("Try your own review")
user_review = st.text_area("Paste a review to see live sentiment + aspect prediction")
if st.button("Analyze") and user_review:
    # TODO: run model.predict + aspects.extract_aspect_sentences on user_review
    st.write("Model output goes here")

st.caption("Model info: F1 = TODO | Dataset: Yelp Open Dataset (Philadelphia, Tucson) | [GitHub](#)")
