import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from src.features.build_features import build_features

DATA_PATH = "data/sample/sample_p2p_payments.csv"
MODEL_PATH = "src/models/p2p_fraud_model.joblib"

FEATURES = [
    "payment_amount", "amount_deviation_score", "payments_1h", "recipient_age_days",
    "recipient_risk_score", "auth_failure_count", "device_risk_score", "proxy_risk_score",
    "behavioral_anomaly_score", "typing_cadence_deviation", "touch_gesture_anomaly",
    "navigation_anomaly_score", "mule_network_risk_score", "rapid_dispersal_score",
    "graph_community_risk_score", "high_payment_velocity_flag", "new_recipient_flag",
    "high_device_risk_flag", "behavioral_anomaly_flag", "high_graph_risk_flag"
]

def train():
    df = build_features(pd.read_csv(DATA_PATH))
    X = df[FEATURES]
    y = df["fraud_label"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42
    )
    model = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(X_test), zero_division=0))
    joblib.dump(model, MODEL_PATH)

if __name__ == "__main__":
    train()
