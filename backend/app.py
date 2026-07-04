from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)  # tells the server to accept requests from react

# 1. load from train.py
print("Loading")
knn_model = joblib.load("model/knn_model.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")
df_products = pd.read_pickle("model/df.pkl")
print("Assets loaded successfully!")

@app.route("/api/recommend", methods=["POST"])
def recommend():
    # eventually take the incoming keywords, convert them to a vector and find the nearest neighbors
    # runs right now, recommendation work to be done
    return jsonify({"message": "Server is listening!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

