class ExecutiveKPIEngine:

    def calculate(self, event):

        confidence = event.get("confidence", 0)

        return {
            "AI_CONFIDENCE": confidence,
            "DECISION_HEALTH":
                "GREEN" if confidence >= 0.9 else "YELLOW",
            "ACTIVE_DECISIONS": 1,
            "RISK_SCORE": event.get("risk_score", 0),
        }
