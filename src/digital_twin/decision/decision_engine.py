class DecisionEngine:
    """
    Generate possible decisions from digital twin situation.
    """

    def evaluate(self, twin_state):

        decisions = []

        for risk in twin_state.risks:

            if risk["type"] == "cold_chain_breach":

                decisions.append({
                    "action": "move_to_backup_storage",
                    "reason": "Prevent product quality loss",
                    "priority": "high"
                })

            elif risk["type"] == "capacity_shortage":

                decisions.append({
                    "action": "optimize_capacity",
                    "reason": "Reduce operational congestion",
                    "priority": "medium"
                })

        twin_state.decisions = decisions

        return twin_state
