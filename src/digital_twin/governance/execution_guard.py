class ExecutionGuard:
    """
    Validate action before execution.
    """

    def validate(self, action):

        blocked_actions = [
            "delete_inventory",
            "shutdown_system"
        ]

        if action in blocked_actions:
            return {
                "allowed": False,
                "reason": "Policy restriction"
            }

        return {
            "allowed": True,
            "reason": "Policy approved"
        }
