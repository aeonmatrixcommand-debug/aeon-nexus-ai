class OpportunityEngine:
    """
    Detect business opportunities from signals.
    """

    def detect(self, insights):

        opportunities = []

        for item in insights["insights"]:

            if item["type"] == "cost_risk":

                opportunities.append({
                    "opportunity":
                        "route_optimization",
                    "reason":
                        "Reduce transportation impact"
                })


        return opportunities
