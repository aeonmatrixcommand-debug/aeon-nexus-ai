import json
from datetime import datetime


class KnowledgeGraph:

    def __init__(self):
        self.nodes = []
        self.relationships = []


    def add_entity(self, entity_type, name, attributes=None):

        node = {
            "id": f"{entity_type}-{len(self.nodes)+1}",
            "type": entity_type,
            "name": name,
            "attributes": attributes or {}
        }

        self.nodes.append(node)

        return node


    def add_relationship(self, source, relation, target):

        self.relationships.append({
            "source": source["id"],
            "relation": relation,
            "target": target["id"]
        })


    def query_context(self):

        return {
            "graph_timestamp":
                datetime.utcnow().isoformat(),

            "entities":
                self.nodes,

            "relationships":
                self.relationships,

            "status":
                "CONTEXT_READY"
        }


if __name__ == "__main__":

    graph = KnowledgeGraph()

    warehouse = graph.add_entity(
        "WAREHOUSE",
        "DC-PRIMARY",
        {
            "kpi": "OTIF",
            "status": "RISK"
        }
    )

    inventory = graph.add_entity(
        "INVENTORY",
        "SKU-CRITICAL",
        {
            "shelf_life": "LOW",
            "risk": "HIGH"
        }
    )

    driver = graph.add_entity(
        "TRANSPORT",
        "DRIVER-FLEET-01",
        {
            "eta_status": "UNSTABLE"
        }
    )


    graph.add_relationship(
        warehouse,
        "CONTAINS",
        inventory
    )

    graph.add_relationship(
        driver,
        "IMPACTS",
        warehouse
    )


    print("=" * 60)
    print(" AEON MATRIX KNOWLEDGE GRAPH INTELLIGENCE")
    print("=" * 60)

    print(json.dumps(
        graph.query_context(),
        indent=2
    ))
