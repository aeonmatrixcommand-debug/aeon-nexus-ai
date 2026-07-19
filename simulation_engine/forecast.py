class ScenarioForecastEngine:

    def forecast(self, simulation):

        if simulation["impact_level"] == "HIGH":
            action = "Activate Recovery Plan"

        elif simulation["impact_level"] == "MEDIUM":
            action = "Inventory Optimization"

        else:
            action = "Continue Monitoring"

        return {
            "forecast_status": "READY",
            "recommended_action": action,
            "confidence": "HIGH"
        }
