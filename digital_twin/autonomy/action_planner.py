class ActionPlanner:
    """
    Convert intelligence into executable actions.
    """

    def plan(self, insight):

        actions = []

        if insight == "cold_chain_breach":
            actions.append({
                "action": "reroute_inventory",
                "priority": "critical",
                "expected_recovery": 0.82
            })

            actions.append({
                "action": "notify_customer",
                "priority": "high",
                "expected_recovery": 0.65
            })

        return actions
