class ConfidenceEvaluator:

    def evaluate(self, action):
        risk = action.get("risk_level", "LOW")

        scores = {
            "LOW": 0.95,
            "MEDIUM": 0.85,
            "HIGH": 0.75,
            "CRITICAL": 0.90
        }

        return scores.get(risk, 0.5)
