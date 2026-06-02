from src.inference.score_payment import reason_codes

def test_new_recipient_reason_code():
    reasons = reason_codes({
        "recipient_age_days": 1,
        "payments_1h": 1,
        "amount_deviation_score": 0.1,
        "device_risk_score": 0.1,
        "behavioral_anomaly_score": 0.1,
        "mule_network_risk_score": 0.1,
        "rapid_dispersal_score": 0.1
    })
    assert "New recipient risk" in reasons
