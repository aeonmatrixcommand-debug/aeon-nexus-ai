class PreventionEngine:


    def recommend(self, root_cause):


        if root_cause["root_cause"] == "cooling_system_deviation":

            return {

                "prevention":

                "predictive_maintenance",

                "action":

                "schedule_equipment_check",

                "risk_reduction":

                0.90

            }


        return {

            "prevention":

            "monitoring",

            "risk_reduction":

            0.50

        }
