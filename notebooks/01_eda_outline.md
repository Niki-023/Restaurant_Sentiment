# Phase 2: Data acquisition & EDA — notebook outline

Turn this into `01_eda.ipynb`. Work through in order; don't skip to modeling.

1. **Load & filter**
   - Load `business.json`, filter to restaurants in Philadelphia + Tucson
   - Stream-filter `review.json` to just those business_ids (see `data/raw/README.md`)
   - Save the filtered result to `data/processed/reviews_filtered.parquet` so you
     never have to re-do this slow step again

2. **Basic shape**
   - How many restaurants? How many reviews? Reviews per restaurant (min/median/max)?
   - Any restaurants with too few reviews to be useful (e.g. < 10)? Decide a cutoff.

3. **Rating distribution**
   - Plot star rating distribution — Yelp is usually skewed toward 4-5 stars.
   - This matters: if 70% of reviews are positive, your sentiment model needs
     class balancing (`class_weight="balanced"`, or resampling) or it'll just
     predict "positive" for everything and still look accurate.

4. **Text characteristics**
   - Review length distribution (words). Any near-empty or spammy reviews?
   - Check for duplicate reviews (copy-pasted spam happens on Yelp)

5. **Aspect keyword coverage (sanity check for src/aspects.py)**
   - For a sample of reviews, check what % contain each aspect keyword set
   - If "ambiance" keywords barely appear, you may need to expand that keyword list

6. **Define the sentiment label**
   - Apply `rating_to_sentiment_label()` from `src/preprocessing.py`
   - Check the resulting class balance (negative/neutral/positive counts)

7. **Train/test split — do this now, not later**
   - Split by review (or by restaurant, if you want to test generalization to
     unseen restaurants — worth trying both and noting the difference)
   - Save the split so every later notebook uses the exact same test set

### Output of this notebook
- `data/processed/reviews_filtered.parquet` — cleaned, filtered dataset
- `data/processed/train.parquet`, `data/processed/test.parquet`
- A written summary (markdown cells) of what you found — this becomes part
  of your README's "Results" section later
