class DashboardOptimizer:

    def generate(self, situation):

        if situation == "critical":

            return [
                "risk",
                "impact",
                "recommended_action",
                "simulation"
            ]

        return [
            "health",
            "performance"
        ]
