class PolicyRules:

    def evaluate(self, action):

        risk = action.get(
            "risk_level",
            "LOW"
        )

        if risk == "CRITICAL":
            return {
                "decision": "APPROVE",
                "reason": "critical action requires controlled execution",
                "risk_score": 90
            }

        if risk == "HIGH":
            return {
                "decision": "ESCALATE",
                "reason": "high risk requires guardian review",
                "risk_score": 70
            }

        return {
            "decision": "APPROVE",
            "reason": "low risk action",
            "risk_score": 20
        }
