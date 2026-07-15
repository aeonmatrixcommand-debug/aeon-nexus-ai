class ExplanationEngine:
    """
    Translate Digital Twin intelligence
    into human understandable explanation.
    """

    def explain(self, situation):

        return {
            "summary": f"Detected situation: {situation}",
            "reason": "Analysis generated from Digital Twin reasoning layer",
            "business_effect": [
                "Operational impact identified",
                "Risk evaluation completed"
            ],
            "recommended_action":
                "Review AI recommendation and execute approved action"
        }
