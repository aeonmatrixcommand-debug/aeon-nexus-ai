class ScenarioForecaster:
    """
    Simulate possible future scenarios.
    """

    def forecast(self, scenario):

        if scenario == "do_nothing":
            return {
                "otif": 0.86,
                "cost_change": 0.14,
                "risk": "high"
            }

        if scenario == "increase_capacity":
            return {
                "otif": 0.97,
                "cost_change": 0.05,
                "risk": "low"
            }

        return {
            "otif": 0,
            "risk": "unknown"
        }
