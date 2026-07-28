class PredictionEngine:

    def predict(self, data):
        return {
            "forecast": data,
            "confidence": 0.90
        }
