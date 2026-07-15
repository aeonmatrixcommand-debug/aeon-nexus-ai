class ScenarioBuilder:
    """
    Build possible future scenarios.
    """

    def build(self, decision):

        return [
            {
                "scenario": "execute_action",
                "action": decision,
                "mode": "active"
            },
            {
                "scenario": "do_nothing",
                "action": None,
                "mode": "passive"
            }
        ]
