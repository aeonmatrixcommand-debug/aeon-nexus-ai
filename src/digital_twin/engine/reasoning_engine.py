class ReasoningEngine:
    """
    Explain digital twin decisions
    between AI and human operators.
    """

    def explain(self, risk):

        explanation = {
            "risk_type": risk.get("type"),
            "reason": "",
            "confidence": 0,
            "recommended_action": ""
        }

        if risk.get("type") == "cold_chain_breach":

            explanation["reason"] = (
                "Temperature exceeded allowed cold chain threshold"
            )

            explanation["confidence"] = 0.91

            explanation["recommended_action"] = (
                "Move affected inventory to backup cold storage"
            )


        elif risk.get("type") == "capacity_shortage":

            explanation["reason"] = (
                "Warehouse workload exceeds available capacity"
            )

            explanation["confidence"] = 0.86

            explanation["recommended_action"] = (
                "Reallocate workforce and optimize picking wave"
            )

        return explanation
