import pandas as pd
import json

# Reload business data, filter to our 2 cities' restaurants
business = pd.read_json("../data/raw/yelp_academic_dataset_business.json", lines=True)
restaurants = business[
    business["categories"].str.contains("Restaurants", na=False)
    & business["city"].isin(["Philadelphia", "Tucson"])
]
print(f"Restaurants in scope: {len(restaurants)}")

business_ids = set(restaurants["business_id"])

# Stream through review.json line by line, keep only matching reviews
matched_reviews = []
with open("../data/raw/yelp_academic_dataset_review.json", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        review = json.loads(line)
        if review["business_id"] in business_ids:
            matched_reviews.append(review)
        if i % 500_000 == 0:
            print(f"Processed {i} lines, matched {len(matched_reviews)} so far...")

print(f"Total matched reviews: {len(matched_reviews)}")

reviews_df = pd.DataFrame(matched_reviews)

# Save both filtered datasets so we never have to redo this slow step
restaurants.to_parquet("../data/processed/restaurants_filtered.parquet", index=False)
reviews_df.to_parquet("../data/processed/reviews_filtered.parquet", index=False)
print("Saved filtered datasets to data/processed/")