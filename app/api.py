from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

# Load trained ML model
model = joblib.load("model/ecocart_model.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "Eco-Cart AI API is running!"
    })


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    product = pd.DataFrame({
        "category": [data["category"]],
        "material": [data["material"]],
        "weight_g": [data["weight_g"]],
        "packaging": [data["packaging"]],
        "recyclable": [data["recyclable"]],
        "reusable": [data["reusable"]],
        "durability_years": [data["durability_years"]],
        "certification": [data["certification"]]
    })

    prediction = model.predict(product)

    eco_score = float(prediction[0])

    # Keep score between 0 and 100
    eco_score = max(0, min(100, eco_score))

    if eco_score >= 80:
        level = "Highly Eco-Friendly"
    elif eco_score >= 60:
        level = "Moderately Eco-Friendly"
    elif eco_score >= 40:
        level = "Less Eco-Friendly"
    else:
        level = "Not Eco-Friendly"

    return jsonify({
        "eco_score": round(eco_score, 2),
        "level": level
    })


if __name__ == "__main__":
    app.run(debug=True)