import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

# Define dataset path
base_dir = r"C:\Users\Shashank Mahato\Desktop\DataHaemScan\ppg_data"

# Load datasets
X_train = pd.read_csv(os.path.join(base_dir, "X_train.csv"))
X_test = pd.read_csv(os.path.join(base_dir, "X_test.csv"))
y_train = pd.read_csv(os.path.join(base_dir, "y_train.csv"))
y_test = pd.read_csv(os.path.join(base_dir, "y_test.csv"))

# Ensure y_train and y_test are continuous values (hemoglobin levels)
y_train = y_train.squeeze()  # Convert to 1D array if needed
y_test = y_test.squeeze()

# 🔹 Select only the first 12 features (ignore extras)
expected_features = 12
if X_train.shape[1] > expected_features:
    print(f"Warning: Trimming {X_train.shape[1] - expected_features} extra features.")
    X_train = X_train.iloc[:, :expected_features]
    X_test = X_test.iloc[:, :expected_features]

# Train a RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Performance:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Save the trained model
model_path = os.path.join(base_dir, "ppg_model.pkl")
joblib.dump(model, model_path)

print(f"Model saved successfully at: {model_path}")
