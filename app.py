from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.data_science.pipeline.predictionpipeline import PredictionPipleine

app = Flask(__name__)

@app.route('/', methods=["GET"])
def homepage():
    return render_template("index.html")  # fixed path

@app.route('/train', methods=["GET"])
def training():
    os.system("python main.py")
    return "Training Successful"

@app.route('/predict', methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        try:
            data = [
                float(request.form["fixed_acidity"]),
                float(request.form["volatile_acidity"]),
                float(request.form["citric_acid"]),
                float(request.form["residual_sugar"]),
                float(request.form["chlorides"]),
                float(request.form["free_sulfur_dioxide"]),
                float(request.form["total_sulfur_dioxide"]),
                float(request.form["density"]),
                float(request.form["pH"]),
                float(request.form["sulphates"]),
                float(request.form["alcohol"])
            ]
            data = np.array(data).reshape(1, -1)
            obj = PredictionPipleine()
            prediction = obj.predict(data)
            return render_template("results.html", prediction=prediction)
        except Exception as e:
            return f"Something went wrong: {e}"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)