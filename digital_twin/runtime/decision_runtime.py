from types import SimpleNamespace


class DecisionRuntime:
    def __init__(self):
        self.status = "READY"

    def execute(self, twin):
        return SimpleNamespace(
            decision_result={
                "recommendation": {
                    "action": "move_to_backup_storage"
                },
                "status": self.status
            }
        )
