def explain_p2p_risk(payment: dict) -> dict:
    return {
        "explanation_type": "reason_code_and_feature_attribution_stub",
        "features_reviewed": list(payment.keys()),
        "note": "Replace with SHAP, graph explanation, or another approved explainability method."
    }
