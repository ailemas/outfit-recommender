"""
train.py
Trains a KNN model on the preprocessed feature matrix and saves it to disk.
Run once before starting app.py.

Usage:
    python train.py
"""

import os
import joblib
from sklearn.neighbors import NearestNeighbors
from preprocess import load_and_preprocess

MODEL_DIR = "model"


# Trains a KNN model on the preprocessed feature matrix and saves it to disk
def train_and_save(n_neighbors: int = 10):
    # Load preprocessed data
    df, features = load_and_preprocess()

    # Start training KNN model
    print("Training KNN model ...")
    # Use cosine distance for similarity search
    knn = NearestNeighbors(
        n_neighbors=n_neighbors,
        metric="cosine",
        algorithm="brute",  # required for cosine
    )
    # Fit the model
    knn.fit(features)

    # Save the model & feature columns to disk
    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(knn, f"{MODEL_DIR}/knn_model.pkl")
    joblib.dump(list(features.columns), f"{MODEL_DIR}/feature_columns.pkl")
    df.to_pickle(f"{MODEL_DIR}/df.pkl")

    print(f"Saved model to {MODEL_DIR}/")
    return knn, list(features.columns), df

# Return:
#     knn: Trained KNN model
#     feature_columns: List of feature column names
#     df: Original DataFrame


if __name__ == "__main__":
    train_and_save()

