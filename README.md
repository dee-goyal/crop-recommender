# AgriSage – Your Smart Crop Advisor

**Live Demo:** [https://recommendation-system-u1iy.onrender.com/](https://recommendation-system-u1iy.onrender.com/)

---

## 🔍 Overview

AgriSage is an intelligent Flask-based crop recommendation system that empowers farmers and agricultural planners with data-driven insights. By analyzing key soil and climate parameters—**Nitrogen (N)**, **Phosphorus (P)**, **Potassium (K)**, **Temperature (°C)**, **Humidity (%)**, **pH**, and **Rainfall (mm)**—it instantly predicts the most suitable crop to cultivate under specific field conditions.

---

## 🚀 Features

* **Interactive Web UI** built with Flask and Jinja2 for seamless user interaction
* **Real-time Predictions** via a pre-trained Random Forest Classifier
* **Hyperparameter-Tuned** for optimal accuracy using GridSearchCV and 5-fold cross-validation
* **Robust Preprocessing** with Label Encoding and Standard Scaling
* **Production-Ready** deployment with Gunicorn or Flask’s built-in server

---

## 📂 Repository Structure

```
.
├── api/                         # Flask application code
│   └── crop_recommender_app.py
├── templates/                   # HTML templates for the web UI
│   └── index.html
├── crop_data.csv               # Original dataset
├── Crop-Recommender.pkl        # Trained Random Forest model
├── Feature-Scaler.pkl          # Trained StandardScaler
├── Label-Encoder.pkl           # Trained LabelEncoder
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version for Render (python-3.8.10)
├── render.yaml                 # Render build configuration
└── README.md                   # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/dee-goyal/recommendation_system.git
   cd recommendation_system
   ```
2. **Create & activate a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\\Scripts\\activate   # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the App Locally

* **Development mode** (Flask server):

  ```bash
  python api/crop_recommender_app.py
  ```
* **Production mode** (Gunicorn):

  ```bash
  gunicorn api.crop_recommender_app:app
  ```

Then open `http://localhost:5000`.

---

## 🧠 Model Details

* **Algorithm:** Random Forest Classifier
* **Tuning:** GridSearchCV over hyperparameters with 5-fold CV
* **Preprocessing:** LabelEncoder for crop labels, StandardScaler for features
* **Artifacts:** `Crop-Recommender.pkl`, `Feature-Scaler.pkl`, `Label-Encoder.pkl`

---

## 🌐 Deployment

Live on Render: [https://recommendation-system-u1iy.onrender.com/](https://recommendation-system-u1iy.onrender.com/)

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ by the AgriSage Team</p>
