def behavioral_reason_codes(behavior: dict) -> list:
    reasons = []
    if behavior.get("typing_cadence_deviation", 0) >= 0.7:
        reasons.append("Typing cadence mismatch")
    if behavior.get("touch_gesture_anomaly", 0) >= 0.7:
        reasons.append("Touch gesture anomaly")
    if behavior.get("navigation_anomaly_score", 0) >= 0.7:
        reasons.append("Abnormal payment navigation behavior")
    if behavior.get("transaction_hesitation_score", 0) >= 0.7:
        reasons.append("Unusual payment hesitation pattern")
    return reasons
