
class PolicyGuard:


    def validate(self, action):

        blocked = [
            "DELETE",
            "SHUTDOWN",
            "RESET"
        ]


        name = action.get(
            "action",
            ""
        )


        if name in blocked:
            return {
                "allowed": False,
                "reason": "Safety policy blocked"
            }


        return {
            "allowed": True,
            "reason": "Approved"
        }
