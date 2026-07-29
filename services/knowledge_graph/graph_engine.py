class KnowledgeGraph:

    def add_node(self, entity):
        return {
            "entity": entity,
            "added": True
        }

    def connect(self, source, target):
        return {
            "source": source,
            "target": target,
            "connected": True
        }
