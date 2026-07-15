class AgentDiscovery:

    def __init__(
        self,
        catalog,
        capability_index
    ):
        self.catalog = catalog
        self.capability_index = capability_index


    def find(
        self,
        capability
    ):

        agent_name = self.capability_index.search(
            capability
        )

        if agent_name is None:
            return None

        return self.catalog.get(
            agent_name
        )
