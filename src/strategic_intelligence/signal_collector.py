class SignalCollector:


    def collect(self):

        return [

            {
                "signal":"market_demand_change",
                "value":"increase",
                "confidence":0.88
            },

            {
                "signal":"transport_cost_change",
                "value":"rising",
                "confidence":0.82
            },

            {
                "signal":"regional_supply_risk",
                "value":"medium",
                "confidence":0.79
            }

        ]
