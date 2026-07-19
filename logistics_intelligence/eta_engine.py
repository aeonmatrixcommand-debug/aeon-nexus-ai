class ETAPredictionEngine:

    def predict(self, distance, traffic):

        delay = distance * traffic

        return {
            "eta_prediction": "CALCULATED",
            "delay_minutes": delay,
            "confidence": "HIGH"
        }
