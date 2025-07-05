
from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)


# Update these lines to use absolute paths
import os
model_path = os.path.join(os.path.dirname(__file__), "Crop-Recommender.pkl")
encoder_path = os.path.join(os.path.dirname(__file__), "Label-Encoder.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "Feature-Scaler.pkl")

model = joblib.load(model_path)
encoder = joblib.load(encoder_path)
scaler = joblib.load(scaler_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        nitrogen  = float(request.form.get("nitrogenBox", 0))
        phosphorus = float(request.form.get("phosphorusBox", 0))
        potassium  = float(request.form.get("potassiumBox", 0))
        temperature = float(request.form.get("temperatureBox", 0))
        humidity    = float(request.form.get("humidityBox", 0))
        ph_value    = float(request.form.get("phBox", 0))
        rainfall    = float(request.form.get("rainfallBox", 0))
    except ValueError:
        return render_template(
            'index.html',
            prediction_text="Invalid input: please enter numeric values for all fields.",
            form_data=request.form.to_dict()
        )

   
    features = np.array([nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]).reshape(1, -1)
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)
    crop_name = encoder.inverse_transform(prediction)[0]

    return render_template(
        'index.html',
        prediction_text=f'The recommended crop is {crop_name}',
        form_data=request.form.to_dict()
    )

if __name__ == "__main__":
    app.run(debug=True)
