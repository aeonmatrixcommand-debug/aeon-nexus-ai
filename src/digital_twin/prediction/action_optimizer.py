class ActionOptimizer:
    """
    Select best action from predicted risks.
    """

    def optimize(self, risk):

        if risk:

            return {
                "recommended_action": "reroute",
                "impact_reduction": 0.72,
                "confidence": 0.89
            }

        return {
            "recommended_action": "none",
            "impact_reduction": 0,
            "confidence": 0
        }
