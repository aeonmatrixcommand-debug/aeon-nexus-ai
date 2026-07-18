from mother_brain.decision import DecisionEngine


class MotherBrain:

    def __init__(self):
        self.decision = DecisionEngine()

    def analyze(self, event):

        return self.decision.process(
            "Inventory Re-Sync"
        )
