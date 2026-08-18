import pandas as pd

business = pd.read_json("../data/raw/yelp_academic_dataset_business.json", lines=True)
print(f"Total businesses: {len(business)}")

restaurants = business[business["categories"].str.contains("Restaurants", na=False)]
print(f"Total restaurants: {len(restaurants)}")

print(restaurants["city"].value_counts().head(15))