class OpportunityDetector:
    """
    Detect business opportunities.
    """

    def detect(self, intelligence):

        opportunities = []

        if intelligence["market_trend"] == "changing":

            opportunities.append(
                "demand_shift_opportunity"
            )

        return {
            "opportunities": opportunities,
            "status": "detected"
        }
