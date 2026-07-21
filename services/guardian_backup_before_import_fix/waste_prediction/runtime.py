class WastePredictionEngine:

    def predict(self, item):
        expiry = item.get("expiry_risk", 0)

        return {
            "waste_probability": expiry,
            "status": "high" if expiry >= 0.7 else "low"
        }
