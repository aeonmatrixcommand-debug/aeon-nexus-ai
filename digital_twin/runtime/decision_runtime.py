from types import SimpleNamespace

class DecisionRuntime:
    def __init__(self):
        self.status = "READY"

    def execute(self, twin):
        return {"status": self.status}
