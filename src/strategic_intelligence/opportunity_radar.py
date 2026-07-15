class OpportunityRadar:


    def analyze(self, signals):


        opportunities=[]


        for signal in signals:


            if signal["signal"]=="market_demand_change":

                opportunities.append(
                    {
                    "opportunity":
                    "increase_inventory_position",

                    "reason":
                    "Demand growth detected",

                    "confidence":
                    signal["confidence"]
                    }
                )


            if signal["signal"]=="transport_cost_change":

                opportunities.append(
                    {
                    "opportunity":
                    "optimize_transport_network",

                    "reason":
                    "Cost pressure detected",

                    "confidence":
                    signal["confidence"]
                    }
                )


        return {

            "opportunities": opportunities,

            "radar_status":
            "completed"

        }
