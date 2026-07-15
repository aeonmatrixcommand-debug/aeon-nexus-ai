class ExecutiveEngine:
    """
    Generate executive recommendation.
    """

    def decide(self, analysis):

        if analysis["opportunities"]:

            return {
                "decision":
                    "optimize_logistics",
                "priority":
                    "high",
                "reason":
                    "Opportunity detected"
            }

        return {
            "decision":
                "monitor",
            "priority":
                "normal"
        }
