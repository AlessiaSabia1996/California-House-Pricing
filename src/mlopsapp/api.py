from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("src/model.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    if not data or "features" not in data:
        return jsonify({"error": "Must provide 8 numerical features"}), 400

    features = data['features']

    if len(features) != 8:
        return jsonify({"Some feature is missing!"}), 400
    
    prediction = model.predict([features])
    return jsonify({"prediction": float(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)