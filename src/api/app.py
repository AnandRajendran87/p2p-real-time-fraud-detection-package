from fastapi import FastAPI
from pydantic import BaseModel
from src.inference.score_payment import score_payment

app = FastAPI(title="Real-Time P2P Fraud Detection API")

class P2PPayment(BaseModel):
    payment_amount: float
    amount_deviation_score: float
    payments_1h: int
    recipient_age_days: int
    recipient_risk_score: float
    auth_failure_count: int
    device_risk_score: float
    proxy_risk_score: float
    behavioral_anomaly_score: float
    typing_cadence_deviation: float
    touch_gesture_anomaly: float
    navigation_anomaly_score: float
    mule_network_risk_score: float
    rapid_dispersal_score: float
    graph_community_risk_score: float

@app.get("/")
def health_check():
    return {"status": "ok", "service": "p2p-real-time-fraud-detection"}

@app.post("/score-payment")
def score(payment: P2PPayment):
    return score_payment(payment.model_dump())
