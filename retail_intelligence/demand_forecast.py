class DemandForecastEngine:

    def forecast(self, history):

        if history > 1000:
            level = "HIGH_DEMAND"
        elif history > 500:
            level = "NORMAL_DEMAND"
        else:
            level = "LOW_DEMAND"

        return {
            "forecast_status": "READY",
            "demand_level": level,
            "confidence": "HIGH"
        }
