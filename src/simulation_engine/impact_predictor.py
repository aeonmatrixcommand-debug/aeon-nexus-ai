class ImpactPredictor:
    """
    Predict business impact.
    """

    def predict(self, scenario):

        if scenario["mode"] == "active":

            return {
                "risk_change": -0.85,
                "cost": 12000,
                "sla": "protected"
            }


        return {
            "risk_change": 0.60,
            "cost": 0,
            "sla": "at_risk"
        }
