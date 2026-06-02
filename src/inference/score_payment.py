import joblib
import pandas as pd
from src.features.build_features import build_features

FEATURES = [
    "payment_amount", "amount_deviation_score", "payments_1h", "recipient_age_days",
    "recipient_risk_score", "auth_failure_count", "device_risk_score", "proxy_risk_score",
    "behavioral_anomaly_score", "typing_cadence_deviation", "touch_gesture_anomaly",
    "navigation_anomaly_score", "mule_network_risk_score", "rapid_dispersal_score",
    "graph_community_risk_score", "high_payment_velocity_flag", "new_recipient_flag",
    "high_device_risk_flag", "behavioral_anomaly_flag", "high_graph_risk_flag"
]

def reason_codes(payment: dict) -> list:
    reasons = []
    if payment.get("recipient_age_days", 999) <= 2:
        reasons.append("New recipient risk")
    if payment.get("payments_1h", 0) >= 5:
        reasons.append("High payment velocity")
    if payment.get("amount_deviation_score", 0) >= 0.7:
        reasons.append("Payment amount deviates from historical behavior")
    if payment.get("device_risk_score", 0) >= 0.7:
        reasons.append("High device risk")
    if payment.get("behavioral_anomaly_score", 0) >= 0.7:
        reasons.append("Behavioral anomaly detected")
    if payment.get("mule_network_risk_score", 0) >= 0.7:
        reasons.append("Potential mule account network connection")
    if payment.get("rapid_dispersal_score", 0) >= 0.7:
        reasons.append("Rapid fund dispersal indicator")
    return reasons

def score_payment(payment: dict, model_path: str = "src/models/p2p_fraud_model.joblib") -> dict:
    model = joblib.load(model_path)
    df = build_features(pd.DataFrame([payment]))
    probability = float(model.predict_proba(df[FEATURES])[0][1])
    if probability >= 0.85:
        decision = "BLOCK_PAYMENT"
    elif probability >= 0.65:
        decision = "TEMPORARY_HOLD_AND_REVIEW"
    elif probability >= 0.45:
        decision = "STEP_UP_AUTHENTICATION"
    else:
        decision = "ALLOW_PAYMENT"
    return {
        "p2p_fraud_probability": round(probability, 4),
        "decision": decision,
        "reason_codes": reason_codes(payment)
    }
