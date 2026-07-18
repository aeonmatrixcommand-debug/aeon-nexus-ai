class PolicyEngine:

    RULES = {
        "NO_SCAN_NO_MOVE": True,
        "WEIGHT_VERIFICATION_REQUIRED": True,
        "ROUTE_CHANGE_REQUIRES_APPROVAL": True
    }


    def evaluate(self, action):

        normalized = action.lower()

        if "route" in normalized:
            return {
                "decision": "REQUIRES_APPROVAL",
                "reason": "ROUTE_CHANGE_REQUIRES_APPROVAL"
            }


        if "inventory" in normalized:
            return {
                "decision": "AUTO_EXECUTE",
                "reason": "Inventory correction allowed"
            }


        return {
            "decision": "HUMAN_REVIEW",
            "reason": "Unknown operational action"
        }
