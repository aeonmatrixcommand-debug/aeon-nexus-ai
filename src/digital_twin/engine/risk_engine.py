class RiskEngine:
    """
    Detect operational risks from Digital Twin state.
    """

    def analyze(self, twin_state):

        risks = []

        state = twin_state.current_state

        if state.get("temperature", 0) > 8:
            risks.append(
                {
                    "type": "cold_chain_breach",
                    "severity": "critical",
                    "probability": 0.9
                }
            )

        if state.get("worker_capacity", 100) < 50:
            risks.append(
                {
                    "type": "capacity_shortage",
                    "severity": "high",
                    "probability": 0.75
                }
            )

        for risk in risks:
            twin_state.add_risk(
                risk["type"],
                risk["severity"],
                risk["probability"]
            )

        return twin_state
