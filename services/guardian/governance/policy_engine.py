class PolicyEngine:

    def evaluate(self, decision):

        confidence = decision.get("confidence", 0)

        if confidence < 0.80:
            return {
                "status": "REVIEW",
                "reason": "LOW_CONFIDENCE"
            }

        if decision.get("risk_score", 0) > 0.8:
            return {
                "status": "BLOCK",
                "reason": "HIGH_RISK"
            }

        return {
            "status": "APPROVED",
            "reason": "POLICY_PASS"
        }
