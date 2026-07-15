class CausalAnalyzer:
    """
    Analyze cause-effect relationships.
    """

    def analyze(self, event, decision):

        causes = []

        if event.get("signal") == "temperature_warning":
            causes.append(
                "cold_chain_risk_detected"
            )

        return {
            "event": event,
            "decision": decision,
            "causes": causes,
            "causal_chain": [
                event.get("signal"),
                "risk_detection",
                decision
            ]
        }
