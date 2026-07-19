class ImpactPredictionEngine:

    def predict(self, simulation):

        return {
            "impact_score": 0.9 if simulation["impact"] == "HIGH" else 0.2,
            "prediction": simulation["impact"]
        }
