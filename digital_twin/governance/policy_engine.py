class PolicyEngine:
    """
    Validate AI action against governance rules.
    """

    def check(self, action):

        restricted_actions = [
            "delete_inventory",
            "shutdown_operation"
        ]

        if action in restricted_actions:

            return {
                "allowed": False,
                "approval_required": True,
                "reason": "Restricted action"
            }


        return {
            "allowed": True,
            "approval_required": False,
            "reason": "Policy accepted"
        }
