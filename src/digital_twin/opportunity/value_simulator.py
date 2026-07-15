class ValueSimulator:
    """
    Simulate business value from opportunities.
    """

    def simulate(self, opportunity):

        if opportunity["type"] == "capacity_expansion":
            return {
                "revenue_impact": 0.18,
                "risk_change": -0.12,
                "confidence": 0.86
            }

        if opportunity["type"] == "inventory_optimization":
            return {
                "waste_reduction": 0.25,
                "cost_saving": 0.15,
                "confidence": 0.82
            }

        return {
            "confidence": 0
        }
