"""Flask API for the outfit recommendation system.

Run this file after ``train.py`` has created the model artifacts.
"""

from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from keyword_mapper import extract_keywords, keywords_to_vector


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"
IMAGES_DIR = BASE_DIR / "data" / "images"
DEFAULT_RESULT_COUNT = 8
MAX_RESULT_COUNT = 20

app = Flask(__name__)
CORS(app)

print("Loading model assets...")
knn_model = joblib.load(MODEL_DIR / "knn_model.pkl")
feature_columns = joblib.load(MODEL_DIR / "feature_columns.pkl")
df_products = pd.read_pickle(MODEL_DIR / "df.pkl")
print(f"Assets loaded successfully: {len(df_products)} products")


def parse_result_count(value) -> int:
    """Return a safe requested result count between 1 and MAX_RESULT_COUNT."""
    try:
        count = int(value)
    except (TypeError, ValueError):
        count = DEFAULT_RESULT_COUNT
    return max(1, min(count, MAX_RESULT_COUNT, len(df_products)))


@app.route("/api/recommend", methods=["POST"])
def recommend():
    """Return products matching ``{"keywords": [...], "n": 8}``."""
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    raw_keywords = body.get("keywords", [])
    if not isinstance(raw_keywords, list):
        return jsonify({"error": "'keywords' must be a list of strings."}), 400

    keyword_text = " ".join(
        keyword.strip() for keyword in raw_keywords if isinstance(keyword, str)
    )
    keywords = extract_keywords(keyword_text)
    if not keywords:
        return jsonify({
            "error": (
                "None of those keywords were recognized. Try words like "
                "summer, casual, formal, women, white, dress, glam, or cozy."
            )
        }), 400

    vector = keywords_to_vector(keywords, feature_columns)
    query = pd.DataFrame([vector], columns=feature_columns)
    result_count = parse_result_count(body.get("n", DEFAULT_RESULT_COUNT))
    distances, indices = knn_model.kneighbors(
        query,
        n_neighbors=result_count,
    )

    results = []
    for distance, index in zip(distances[0], indices[0]):
        row = df_products.iloc[index]
        item_id = int(row["id"])
        results.append({
            "id": item_id,
            "name": row["productDisplayName"],
            "gender": row["gender"],
            "subCategory": row["subCategory"],
            "color": row["baseColour"],
            "season": row["season"],
            "usage": row["usage"],
            "similarity": round(max(0.0, 1.0 - float(distance)), 3),
            "image_url": f"/images/{item_id}.jpg",
        })

    return jsonify({
        "keywords": keywords,
        "results": results,
    })


@app.route("/images/<path:filename>")
def get_image(filename):
    """Serve a product image from the local dataset image directory."""
    return send_from_directory(IMAGES_DIR, filename)


@app.route("/api/health")
def health():
    """Provide a small status endpoint for frontend and development checks."""
    return jsonify({"status": "ok", "items": len(df_products)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
