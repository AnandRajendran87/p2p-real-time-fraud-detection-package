def device_reason_codes(device: dict) -> list:
    reasons = []
    if device.get("device_risk_score", 0) >= 0.7:
        reasons.append("High device risk")
    if device.get("proxy_risk_score", 0) >= 0.7:
        reasons.append("High-risk proxy or VPN indicator")
    if device.get("emulator_indicator", 0) == 1:
        reasons.append("Possible emulator usage")
    if device.get("device_age_days", 999) <= 2:
        reasons.append("New or unfamiliar device")
    return reasons
