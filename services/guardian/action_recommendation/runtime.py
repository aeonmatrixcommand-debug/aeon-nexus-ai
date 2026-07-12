class ExecutiveActionRecommendation:

    def recommend(self, situation):
        risk = situation.get("risk", 0)

        if risk >= 0.8:
            return {
                "action": "intervene",
                "priority": "high"
            }

        return {
            "action": "observe",
            "priority": "normal"
        }
