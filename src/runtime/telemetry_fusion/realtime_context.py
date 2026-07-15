class RealTimeContext:

    """
    Convert signals into AI reasoning context.
    """

    def build(self, fusion_result):

        return {
            "context_type": "operational",
            "risk": fusion_result["risk_state"],
            "ready_for_reasoning": True
        }
