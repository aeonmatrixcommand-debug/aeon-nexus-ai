class OpportunityRadar:

    def analyze(self, signals):

        opportunities = []

        text = str(signals).lower()

        if "demand" in text:
            opportunities.append(
                "Demand Optimization Opportunity"
            )

        if "waste" in text:
            opportunities.append(
                "Value Recovery Opportunity"
            )

        if "logistics" in text:
            opportunities.append(
                "Logistics Network Optimization"
            )

        if not opportunities:
            opportunities.append(
                "Continuous Improvement Opportunity"
            )

        return {
            "radar_status": "ACTIVE",
            "opportunities": opportunities
        }
