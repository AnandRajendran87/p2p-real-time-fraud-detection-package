from datetime import datetime, timezone
import json

def create_audit_record(payment_id: str, model_version: str, score_response: dict) -> str:
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "payment_id": payment_id,
        "model_version": model_version,
        "score_response": score_response
    }
    return json.dumps(record, indent=2)
