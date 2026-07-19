class AgentGuard:
    """
    Validate agent actions before execution.
    """

    def validate(self, action):

        if action:

            return {
                "action": action,
                "approved": True,
                "status": "allowed"
            }

        return {
            "approved": False,
            "status": "blocked"
        }
