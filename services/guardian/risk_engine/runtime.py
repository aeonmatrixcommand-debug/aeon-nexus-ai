class RiskEngine:

    def predict(self, signal):
        score = signal.get("risk_signal", 0)

        return {
            "risk_score": score,
            "status": "high" if score >= 0.7 else "normal"
        }
