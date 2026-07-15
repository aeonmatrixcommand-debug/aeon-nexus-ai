class InsightGenerator:
    """
    Generate business insights from Digital Twin situations.
    """

    def generate(self, situation):

        insight = {
            "impact": [],
            "indirect_effects": [],
            "opportunities": []
        }

        if situation["status"] == "attention_required":

            insight["impact"].append(
                "Operational disruption may occur"
            )

            insight["indirect_effects"].append(
                "Customer satisfaction may decrease"
            )

            insight["opportunities"].append(
                "Improve predictive monitoring capability"
            )

        else:

            insight["opportunities"].append(
                "Optimize current operation performance"
            )

        return insight
