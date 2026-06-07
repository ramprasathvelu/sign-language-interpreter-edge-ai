import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# ---------------------------
# LOAD DATA (NO HEADER)
# ---------------------------
data = pd.read_csv("isl_dataset.csv", header=None)

print("Dataset shape:", data.shape)

# ---------------------------
# SPLIT FEATURES & LABELS
# ---------------------------
y = data.iloc[:, 0]      # FIRST COLUMN = LABEL (HELLO, YES, NO)
X = data.iloc[:, 1:]     # REST = 63 FEATURES

print("Labels found:", y.unique())

# ---------------------------
# TRAIN TEST SPLIT
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# ---------------------------
# MODEL
# ---------------------------
model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------------------
# ACCURACY
# ---------------------------
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# ---------------------------
# SAVE MODEL
# ---------------------------
joblib.dump(model, "isl_model.pkl")

print("Model saved successfully ✔")
