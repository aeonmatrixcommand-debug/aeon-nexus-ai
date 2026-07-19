from datetime import datetime


class PredictiveOperationsEngine:

    def analyze(self, event):

        text = event.lower()

        risk = 0
        signals = []

        if "inventory" in text:
            risk += 30
            signals.append("Inventory mismatch")

        if "delay" in text:
            risk += 25
            signals.append("Order delay trend")

        if "eta" in text:
            risk += 20
            signals.append("ETA instability")

        if risk >= 70:
            level = "HIGH"
        elif risk >= 40:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "prediction_engine": "ONLINE",
            "risk_score": risk,
            "risk_level": level,
            "signals": signals,
            "forecast": {
                "next_4_hours": "Monitor bottleneck",
                "next_12_hours": "Optimize operation flow"
            }
        }
