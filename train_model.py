import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Load processed data
df = pd.read_csv("processed_traffic.csv")

print("📊 Processed Data Preview:")
print(df.head())

# Train Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(df)

# Predict anomalies
df["anomaly"] = model.predict(df)  # -1 = anomaly, 1 = normal

# Save model
joblib.dump(model, "anomaly_model.pkl")

# Save results
df.to_csv("anomaly_results.csv", index=False)

print("\n🚨 Model trained successfully!")
print("Model saved as anomaly_model.pkl")
print("Results saved as anomaly_results.csv")