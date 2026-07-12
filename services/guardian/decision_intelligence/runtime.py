class DecisionIntelligence:

    def evaluate(self, context):
        risk = context.get("risk_score", 0)

        if risk >= 0.8:
            return {
                "decision": "escalate",
                "priority": "critical"
            }

        if risk >= 0.5:
            return {
                "decision": "review",
                "priority": "high"
            }

        return {
            "decision": "approve",
            "priority": "normal"
        }
