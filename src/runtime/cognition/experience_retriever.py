class ExperienceRetriever:
    """
    Retrieve previous operational experiences.
    """

    def __init__(self, memory=None):
        self.memory = memory


    def retrieve(self, situation):

        if self.memory:

            return self.memory.history()

        return []
