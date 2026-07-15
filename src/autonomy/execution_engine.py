from digital_twin.governance.execution_guard import ExecutionGuard


class ExecutionEngine:
    """
    Execute approved autonomous actions.
    """

    def __init__(self):

        self.guard = ExecutionGuard()


    def execute(self, action):

        validation = self.guard.validate(
            action
        )

        if validation["allowed"]:

            return {
                "action": action,
                "status": "executed",
                "result": "success"
            }

        return {
            "action": action,
            "status": "blocked",
            "reason": validation["reason"]
        }
