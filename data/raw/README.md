# Getting the data

The Yelp Open Dataset is not auto-downloadable (requires accepting terms on
Yelp's site), so grab it yourself:

1. Go to https://www.yelp.com/dataset
2. Click "Download Dataset," accept the terms
3. You'll get a `.tar` file containing several JSON files — you only need:
   - `yelp_academic_dataset_business.json` (restaurant info: name, city, category, stars)
   - `yelp_academic_dataset_review.json` (the actual review text + rating — this one is large, several GB)
4. Extract both into this `data/raw/` folder

## Filtering to keep it manageable
The review file is huge (7M+ reviews). In `notebooks/01_eda.ipynb`, the first
step will be to:
1. Load `business.json`, filter to `categories` containing "Restaurants" AND
   `city` in `["Philadelphia", "Tucson"]`
2. Get the list of matching `business_id`s
3. Stream through `review.json` line-by-line (it's JSON-lines format) and keep
   only reviews matching those business_ids — do NOT try to load the whole
   file into memory at once, use `pandas.read_json(..., lines=True, chunksize=...)`
   or read line-by-line with the `json` module

This should bring you down to a dataset of a manageable size (tens of
thousands of reviews) that's easy to iterate on.
