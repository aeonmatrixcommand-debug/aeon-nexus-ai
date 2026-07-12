class DemandForecastEngine:

    def forecast(self, data):
        demand = data.get("demand", 0)

        return {
            "forecast": demand,
            "trend": "growth" if demand > 100 else "stable"
        }
