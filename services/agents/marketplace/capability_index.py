class CapabilityIndex:

    def __init__(self):
        self.index = {}

    def add(
        self,
        capability,
        agent_name
    ):
        self.index[capability] = agent_name


    def search(
        self,
        capability
    ):

        return self.index.get(capability)
