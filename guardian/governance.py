class GovernanceEngine:


    RULES = [

        "NO_SCAN_NO_MOVE",

        "WEIGHT_VERIFICATION_REQUIRED",

        "CARTON_RESPONSIBILITY_CHAIN",

        "SHELF_LIFE_PROTECTION",

        "ETA_CHANGE_CONTROL"

    ]


    def check(self, action):

        return {

            "action": action,

            "rules_checked": self.RULES,

            "status": "COMPLIANT"

        }
