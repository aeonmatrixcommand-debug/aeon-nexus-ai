from datetime import datetime


class DecisionOptimizer:

    def evaluate(self, decision_event):

        confidence = decision_event.get(
            "confidence",
            0.0
        )

        score = round(confidence * 100, 2)

        return {
            "decision_score": score,
            "optimization": (
                "IMPROVE"
                if score < 80
                else "OPTIMAL"
            ),
            "timestamp": datetime.utcnow().isoformat()
        }
