"""
- app.py is the flask backend for the outfit recommendation system
- receives keywords, queries the KNN model, and returns matching outfit recommendations as JSON
- run after train.py has been executed

"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from keyword_mapper import keywords_to_vector

app = Flask(__name__)
CORS(app)  # tells the server to accept requests from react

# 1. load from train.py
print("Loading")
knn_model = joblib.load("model/knn_model.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")
df_products = pd.read_csv("data/processed_styles.csv")
print("Assets loaded successfully!")

@app.route("/api/recommend", methods=["POST"])
def recommend():
    """
    Accepts JSON body: { "text": "summer casual women" }
    Returns a JSON array of up to 8 recommended products:
        [{ "id": 1234, "name": "...", "image_url": "/images/1234" }, ...]
    """
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Request body must be JSON."}), 400
 
    text = body.get("text", "").strip()
    if not text:
        return jsonify({"error": "Please provide a 'text' field with your vibe or keywords."}), 400
 
    # split input into keywords
    keywords = text.lower().split()
 
    # convert keywords to vector aligned with the trained model
    try:
        vector = keywords_to_vector(keywords, feature_columns)
    except ValueError:
        return jsonify({
            "error": "None of those keywords were recognized. "
                     "Try words like: summer, casual, formal, women, white, dress, glam, cozy, etc."
        }), 400
 
    # look for 8 closeset matches
    distances, indices = knn_model.kneighbors([vector], n_neighbors=8)
    # look up the matched rows in the metadata CSV (1D row)
    neighbors = df_products.iloc[indices[0]]
 
    results = []
    for index, row in neighbors.iterrows():
        results.append({
            "id":        int(row["id"]),
            "name":      row["productDisplayName"],
            "gender":    row["gender"],
            "colour":    row["baseColour"],
            "season":    row["season"],
            "usage":     row["usage"],
            "image_url": f"/images/{int(row['id'])}"
        })
 
    return jsonify(results)
 
 
@app.route("/images/<int:item_id>")
def get_image(item_id):
    """
    Serves the product image from data/images/<item_id>.jpg.
    Flask returns a 404 automatically if the file is missing —
    the frontend should show a placeholder image in that case.
    """
    return send_from_directory("data/images", f"{item_id}.jpg")



if __name__ == "__main__":
    app.run(debug=True, port=5000)

