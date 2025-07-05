from flask import Flask, request, render_template
import joblib
import numpy as np
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# Model loading with error handling
try:
    model_path = os.path.join(os.path.dirname(__file__), "Crop-Recommender.pkl")
    encoder_path = os.path.join(os.path.dirname(__file__), "Label-Encoder.pkl")
    scaler_path = os.path.join(os.path.dirname(__file__), "Feature-Scaler.pkl")
    
    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
    scaler = joblib.load(scaler_path)
except Exception as e:
    raise RuntimeError(f"Failed to load model files: {str(e)}") from e

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Input validation
        nitrogen = float(request.form.get("nitrogenBox", 0))
        phosphorus = float(request.form.get("phosphorusBox", 0))
        potassium = float(request.form.get("potassiumBox", 0))
        temperature = float(request.form.get("temperatureBox", 0))
        humidity = float(request.form.get("humidityBox", 0))
        ph_value = float(request.form.get("phBox", 0))
        rainfall = float(request.form.get("rainfallBox", 0))
        
        # Range validation
        if not (0 <= ph_value <= 14):
            raise ValueError("pH value must be between 0 and 14")
        if humidity < 0 or humidity > 100:
            raise ValueError("Humidity must be between 0% and 100%")
            
    except ValueError as e:
        return render_template(
            'index.html',
            prediction_text=f"Invalid input: {str(e)}",
            form_data=request.form.to_dict()
        ), 400

    try:
        features = np.array([
            nitrogen, phosphorus, potassium, 
            temperature, humidity, ph_value, rainfall
        ]).reshape(1, -1)
        
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)
        crop_name = encoder.inverse_transform(prediction)[0]
        
        return render_template(
            'index.html',
            prediction_text=f'The recommended crop is {crop_name}',
            form_data=request.form.to_dict()
        )
        
    except Exception as e:
        app.logger.error(f"Prediction failed: {str(e)}")
        return render_template(
            'index.html',
            prediction_text="Sorry, an error occurred while processing your request.",
            form_data=request.form.to_dict()
        ), 500

if __name__ == "__main__":
    # Production configuration - don't use debug=True in production
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    )