# Restaurant Review Sentiment & Recommender

## Problem
People choosing a restaurant have to read dozens of reviews to figure out if
it's actually good, and star ratings alone hide *why* people liked or disliked
it. This tool shows a restaurant's real reputation broken down by what matters
(food, service, ambiance, value), and recommends similar restaurants based on
what people actually praise or complain about — not just cuisine tags.

## Users
- Someone deciding where to eat
- A restaurant owner wanting to understand their own reviews at a glance

## Scope (v1)
- Data: Yelp Open Dataset, filtered to **Philadelphia, PA** and **Tucson, AZ**,
  restaurant category only
- Aspects: keyword-based (food / service / ambiance / value) — v2 candidate:
  swap in a pretrained aspect-sentiment model
- Sentiment: baseline (TF-IDF + Logistic Regression) first, compare against a
  DistilBERT fine-tune

## Success criteria (defined before modeling — do not move the goalposts later)
- Sentiment classifier: F1 ≥ 0.80 on held-out test set
- Recommender: similar-restaurant suggestions pass a manual sanity check on
  ~10 restaurants
- App: results return in under 2-3 seconds per interaction

## Project phases (professional workflow — work through in order)
- [ ] Phase 1: Problem framing — **done, see above**
- [ ] Phase 2: Data acquisition & EDA (`notebooks/01_eda.ipynb`)
- [ ] Phase 3: Baseline model (`notebooks/02_baseline_model.ipynb`)
- [ ] Phase 4: Improved model + evaluation (`notebooks/03_improved_model.ipynb`)
- [ ] Phase 5: Error analysis (`notebooks/04_error_analysis.ipynb`)
- [ ] Phase 6: Package into `src/` modules — **skeleton in place**
- [ ] Phase 7: Build Streamlit app (`app/app.py`) — **skeleton in place**
- [ ] Phase 8: Document results & limitations (this README, filled in at the end)
- [ ] Phase 9: Deploy to Streamlit Community Cloud

## Project structure
```
restaurant-sentiment/
├── data/
│   ├── raw/          # untouched downloaded data (gitignored)
│   └── processed/    # cleaned data, ready for modeling
├── notebooks/         # exploration, prototyping — one notebook per phase
├── src/                # reusable, tested code — the "real" pipeline
│   ├── preprocessing.py
│   ├── sentiment_model.py
│   ├── aspects.py
│   └── recommend.py
├── models/             # saved trained artifacts (gitignored, too large for git)
├── app/
│   └── app.py          # Streamlit app
└── requirements.txt
```

## Results
*(fill in once Phase 4 is done — model metrics, dataset size, key findings)*

## Limitations
*(fill in during Phase 5 error analysis — be honest, this is a strength not a weakness)*

## How to run
```bash
pip install -r requirements.txt
streamlit run app/app.py
```
