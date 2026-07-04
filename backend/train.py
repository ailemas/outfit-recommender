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
    df, features = load_and_preprocess()

    print("Training KNN model ...")
    knn = NearestNeighbors(
        n_neighbors=n_neighbors,
        metric="cosine",
        algorithm="brute",  # required for cosine
    )
    knn.fit(features)

    os.makedirs(MODEL_DIR, exist_ok=True)
    joblib.dump(knn, f"{MODEL_DIR}/knn_model.pkl")
    joblib.dump(list(features.columns), f"{MODEL_DIR}/feature_columns.pkl")
    df.to_pickle(f"{MODEL_DIR}/df.pkl")

    print(f"Saved model to {MODEL_DIR}/")
    return knn, list(features.columns), df


if __name__ == "__main__":
    train_and_save()
