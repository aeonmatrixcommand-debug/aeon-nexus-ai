class SignalIntelligence:
    """
    Interpret external signals.
    """

    def analyze(self, signal_data):

        insights = []

        for signal in signal_data["signals"]:

            if signal == "fuel_price_increase":
                insights.append({
                    "type": "cost_risk",
                    "impact": "transportation_cost_increase"
                })

            elif signal == "weather_disruption":
                insights.append({
                    "type": "operation_risk",
                    "impact": "delivery_delay"
                })

        return {
            "insights": insights,
            "count": len(insights)
        }
