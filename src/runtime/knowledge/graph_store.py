class GraphStore:
    """
    Store knowledge relationships between events,
    decisions, impacts and outcomes.
    """

    def __init__(self):

        self.nodes = []
        self.edges = []


    def add_node(self, node_type, data):

        node = {
            "type": node_type,
            "data": data
        }

        self.nodes.append(node)

        return node


    def add_relationship(self, source, relation, target):

        edge = {
            "source": source,
            "relation": relation,
            "target": target
        }

        self.edges.append(edge)

        return edge


    def view(self):

        return {
            "nodes": self.nodes,
            "edges": self.edges,
            "status": "knowledge_ready"
        }
