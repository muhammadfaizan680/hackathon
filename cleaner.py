import pandas as pd
import numpy as np

def clean_data():
    df = pd.read_csv("../banggood_raw.csv")

    # Clean price
    df['price'] = df['price'].str.replace("$", "", regex=False)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Rating + Reviews
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    df['reviews'] = df['reviews'].str.extract(r'(\d+)')
    df['reviews'] = pd.to_numeric(df['reviews'], errors='coerce')

    # Missing values
    df.fillna({'rating':0, 'reviews':0}, inplace=True)

    # Derived Feature 1: Value Score
    df['value_score'] = (df['rating'] / df['price']).replace([np.inf, -np.inf], 0).fillna(0)

    # Derived Feature 2: Popularity
    df['popularity'] = df['rating'] * df['reviews']

    df.to_csv("../banggood_clean.csv", index=False)
    print("Cleaning Completed! Clean file saved as banggood_clean.csv")

if _name_ == "_main_":
    clean_data()