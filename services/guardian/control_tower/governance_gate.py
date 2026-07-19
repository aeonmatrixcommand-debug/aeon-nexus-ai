class GovernanceGate:

    def approve(self, action):

        blocked = [
            "UNAUTHORIZED_ROUTE_CHANGE",
            "NO_SCAN_NO_MOVE"
        ]

        return {
            "action": action,
            "approved": action not in blocked
        }
