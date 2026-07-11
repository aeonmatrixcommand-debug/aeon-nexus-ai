class RecommendationRuntime:
    def recommend(self, context: dict) -> dict:
        risk = context.get("risk_score", 0.0)

        if risk >= 0.7:
            action = "review"
        elif risk >= 0.3:
            action = "monitor"
        else:
            action = "execute"

        return {
            "action": action,
            "risk_score": risk,
            "confidence": 0.95,
            "explanation": "Rule-based recommendation."
        }
