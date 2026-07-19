class KnowledgeGraph:
    """
    Connect digital twin entities.
    """

    def __init__(self):
        self.nodes = []

    def add_entity(self, entity):

        self.nodes.append(entity)

        return {
            "entity": entity,
            "status": "connected"
        }

    def view(self):

        return self.nodes
