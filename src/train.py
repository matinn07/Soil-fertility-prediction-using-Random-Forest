import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("data/soil_data.csv")

# Target column MUST match your dataset
TARGET_COL = "fertility"

X = df.drop(TARGET_COL, axis=1)
y = df[TARGET_COL]

# Save feature order (VERY IMPORTANT)
feature_names = list(X.columns)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Save model
with open("model/rf_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save feature order
with open("model/features.pkl", "wb") as f:
    pickle.dump(feature_names, f)

print("✅ Model and feature order saved successfully")
