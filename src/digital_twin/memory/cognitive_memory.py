class CognitiveMemory:
    """
    Store connected knowledge relationships.
    """

    def __init__(self):
        self.graph = []

    def remember(self, source, relation, target):

        node = {
            "source": source,
            "relation": relation,
            "target": target
        }

        self.graph.append(node)

        return node

    def recall(self):
        return self.graph
