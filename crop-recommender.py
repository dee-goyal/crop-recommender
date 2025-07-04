import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from joblib import dump, load
import warnings

warnings.filterwarnings('ignore')

crop_df = pd.read_csv("crop_data.csv")
crop_df.rename(columns={'N': 'nitrogen', 'P': 'phosphorus', 'K': 'potassium'}, inplace=True)

feature_cols = ['nitrogen', 'phosphorus', 'potassium', 'temperature', 'humidity', 'ph', 'rainfall']
crop_df = crop_df.drop_duplicates(subset=feature_cols, keep='first')

X = crop_df[feature_cols]
y = crop_df["crop"]

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

X_temp, X_test, y_temp, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, random_state=42, stratify=y_temp
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled   = scaler.transform(X_val)
X_test_scaled  = scaler.transform(X_test)

param_grid = {
    'n_estimators':    [50, 100],
    'max_depth':       [3, 5],
    'min_samples_split': [20, 50],
    'min_samples_leaf':  [10, 20]
}

rf = RandomForestClassifier(random_state=42)

grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)
grid_search.fit(X_train_scaled, y_train)

best_rf = grid_search.best_estimator_

val_preds = best_rf.predict(X_val_scaled)
val_acc = accuracy_score(y_val, val_preds)
print(f"Validation accuracy after tuning: {val_acc:.4f}")
print("Best Random Forest parameters:", grid_search.best_params_)

X_combined = np.vstack((X_train_scaled, X_val_scaled))
y_combined = np.hstack((y_train, y_val))

final_rf = RandomForestClassifier(
    n_estimators=grid_search.best_params_['n_estimators'],
    max_depth=grid_search.best_params_['max_depth'],
    min_samples_split=grid_search.best_params_['min_samples_split'],
    min_samples_leaf=grid_search.best_params_['min_samples_leaf'],
    random_state=42
)
final_rf.fit(X_combined, y_combined)

test_preds = final_rf.predict(X_test_scaled)
test_acc = accuracy_score(y_test, test_preds)
print(f"Test accuracy with tuned Random Forest: {test_acc:.4f}")

cv_scores = cross_val_score(final_rf, scaler.transform(X), y_encoded, cv=5, scoring='accuracy', n_jobs=-1)
print(f"5-fold cross-validation accuracies on entire dataset: {cv_scores}")
print(f"Mean CV accuracy: {cv_scores.mean():.4f}")

dump(final_rf, "Crop-Recommender.pkl")
dump(label_encoder, "Label-Encoder.pkl")
dump(scaler, "Feature-Scaler.pkl")


def predict_crop(input_features):

    model   = load("Crop-Recommender.pkl")
    encoder = load("Label-Encoder.pkl")
    scaler  = load("Feature-Scaler.pkl")

    input_array  = np.array(input_features).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction   = model.predict(input_scaled)
    crop_name    = encoder.inverse_transform(prediction)
    return crop_name[0]
