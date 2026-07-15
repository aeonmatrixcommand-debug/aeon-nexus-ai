class WorldState:
    """
    Shared reality model between human and AI.
    """

    def __init__(self):

        self.human_view = {}
        self.ai_view = {}
        self.shared_context = {}

    def synchronize(self):

        self.shared_context = {
            "human_understanding": self.human_view,
            "ai_reasoning": self.ai_view,
            "aligned": True
        }

        return self.shared_context
