class SituationMemory:

    def __init__(self):
        self.history = []

    def store(self, situation):

        self.history.append({
            "event": situation,
            "timestamp": "now"
        })

        return self.history

    def recall(self):

        return self.history
