import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["high_payment_velocity_flag"] = (df["payments_1h"] >= 5).astype(int)
    df["new_recipient_flag"] = (df["recipient_age_days"] <= 2).astype(int)
    df["high_device_risk_flag"] = (df["device_risk_score"] >= 0.7).astype(int)
    df["behavioral_anomaly_flag"] = (df["behavioral_anomaly_score"] >= 0.7).astype(int)
    df["high_graph_risk_flag"] = (df["graph_community_risk_score"] >= 0.7).astype(int)
    return df
