import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session
import joblib

app = Flask(__name__)
app.secret_key = "supersecretkey"

model = joblib.load("crop_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")

@app.route('/')
def home():
    prediction = session.pop("prediction", None)
    confidence = session.pop("confidence", None)
    return render_template("index.html",
                           prediction_text=prediction,
                           confidence_score=confidence)

@app.route('/predict', methods=['POST'])
def predict():

    data_dict = {
        'N': float(request.form['N']),
        'P': float(request.form['P']),
        'K': float(request.form['K']),
        'temperature': float(request.form['temperature']),
        'humidity': float(request.form['humidity']),
        'ph': float(request.form['ph']),
        'rainfall': float(request.form['rainfall'])
    }

    input_df = pd.DataFrame([data_dict])
    input_scaled = scaler.transform(input_df)

    prediction_encoded = model.predict(input_scaled)
    prediction_label = label_encoder.inverse_transform(prediction_encoded)

    probabilities = model.predict_proba(input_scaled)
    confidence = round(np.max(probabilities) * 100, 2)

    # Store in session
    session["prediction"] = prediction_label[0]
    session["confidence"] = confidence

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)