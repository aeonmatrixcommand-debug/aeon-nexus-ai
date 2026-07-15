class StrategicEngine:
    """
    Convert insights into strategic analysis.
    """

    def analyze(self, insights):

        risks = []
        opportunities = []

        for item in insights:

            if item["type"] == "cost_risk":
                risks.append(
                    "Transportation cost pressure"
                )

                opportunities.append(
                    "Optimize logistics network"
                )

            if item["type"] == "operation_risk":
                risks.append(
                    "Service reliability impact"
                )

        return {
            "risks": risks,
            "opportunities": opportunities
        }
