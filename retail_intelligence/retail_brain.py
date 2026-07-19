class RetailBrain:

    def decide(self, forecast, inventory):

        return {
            "brain_status": "ONLINE",
            "decision": inventory["optimization_action"],
            "forecast": forecast
        }
