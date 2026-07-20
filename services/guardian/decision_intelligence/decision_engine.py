class DecisionIntelligenceEngine:

    def decide(self, impact):

        if impact["priority"] == "HIGH":
            return {
                "decision": "AUTONOMOUS_ACTION",
                "action": "OPTIMIZE_RESOURCE",
                "confidence": impact["business_impact_score"]
            }

        return {
            "decision": "MONITOR",
            "action": "WAIT",
            "confidence": impact["business_impact_score"]
        }
