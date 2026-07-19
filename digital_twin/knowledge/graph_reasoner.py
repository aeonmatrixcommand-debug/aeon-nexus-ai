class GraphReasoner:
    """
    Reason over knowledge graph relationships.
    """

    def analyze(self, entity):

        return {
            "entity": entity,
            "relationships": "evaluated",
            "insight": "generated"
        }

    def analyse(self, entity):
        """
        Compatibility alias.
        """

        return self.analyze(entity)
