class CausalGraph:


    def build(self, event):


        if event["signal"] == "temperature_warning":

            return {

                "event":
                "temperature_warning",

                "causes":[

                    "cooling_system_deviation",

                    "sensor_temperature_change",

                    "equipment_performance_drop"

                ],

                "impact":

                "cold_chain_risk"

            }


        return {

            "event":event,

            "causes":[],

            "impact":"unknown"

        }
