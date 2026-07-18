from datetime import datetime


class ETAPredictionEngine:

    def predict(self, route):

        return {
            "route": route,
            "eta_prediction": "35 minutes",
            "delay_risk": "LOW",
            "generated_at": datetime.utcnow().isoformat()
        }
