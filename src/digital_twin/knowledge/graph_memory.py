class GraphMemory:
    """
    Store historical graph states.
    """

    def __init__(self):
        self.history = []

    def remember(self, state):

        self.history.append(state)

        return {
            "state": state,
            "stored": True
        }

    def recall(self):

        return self.history
