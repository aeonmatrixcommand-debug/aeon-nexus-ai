class DecisionMemory:
    """
    Store AI decisions and outcomes.
    """

    def __init__(self):
        self.decisions = []


    def record(self, decision, result):

        item = {
            "decision": decision,
            "result": result
        }

        self.decisions.append(item)

        return item


    def history(self):

        return self.decisions
