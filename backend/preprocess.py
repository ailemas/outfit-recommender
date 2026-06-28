"""
- preprocess.py loads and cleans styles.csv from Fashion Product Images dataset
- one-hot encodes the dataset into a feature matrix for KNN

"""

import pandas as pd
import numpy as np
import os

# columns in dataset that are used as features for KNN
FEATURE_COLUMNS = ["gender", "subCategory", "baseColour", "season", "usage"]
META_COLUMNS = ["id", "productDisplayName"] + FEATURE_COLUMNS

# returns cleaned metadata dataframe and one-hot encoded dataframe of features for KNN
def load_and_preprocess(csv_path: str = "data/styles.csv"):
    print(f"Loading {csv_path}...")
    
    df = pd.read_csv(csv_path, on_bad_lines="skip") # skip bad lines in csv
    
    df = df.dropna(subset=FEATURE_COLUMNS) # drop rows with missing features
    
    df = df[META_COLUMNS].reset_index(drop=True) # keep columns of interest and reset index
    
    features = pd.get_dummies(df[FEATURE_COLUMNS]) # one-hot encode
    
    print(f"    Items loaded : {len(df)}")
    print(f"    Feature dimensions : {features.shape[1]}")
    return df, features

if __name__ == "__main__":
    df, features = load_and_preprocess()
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/processed_styles.csv", index=False)
    features.to_csv("data/features.csv", index=False)
    print("Saved processed_styles.csv and features.csv")
    print("\nSample feature columns:")
    print(list(features.columns[:20]))
    
    
"""
outputs:

Loading data/styles.csv...
    Items loaded : 44079
    Feature dimensions : 108
Saved processed_styles.csv and features.csv

Sample feature columns:
['gender_Boys', 'gender_Girls', 'gender_Men', 'gender_Unisex', 'gender_Women', 'subCategory_Accessories', 'subCategory_Apparel Set',
'subCategory_Bags', 'subCategory_Bath and Body', 'subCategory_Beauty Accessories', 'subCategory_Belts', 'subCategory_Bottomwear',
'subCategory_Cufflinks', 'subCategory_Dress', 'subCategory_Eyes', 'subCategory_Eyewear', 'subCategory_Flip Flops', 'subCategory_Fragrance',
'subCategory_Free Gifts', 'subCategory_Gloves']
"""

