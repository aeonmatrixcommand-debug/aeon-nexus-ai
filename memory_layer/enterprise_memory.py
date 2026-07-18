from datetime import datetime
import json


class EnterpriseMemory:

    def __init__(self):
        self.memory = []


    def store(self, event, decision, outcome):

        record = {
            "event": event,
            "decision": decision,
            "outcome": outcome,
            "timestamp": datetime.now().isoformat()
        }

        self.memory.append(record)

        return record


    def retrieve(self):

        return self.memory



class KnowledgeGraph:

    def build(self, records):

        graph = {
            "entities": [
                "Warehouse",
                "Inventory",
                "Fleet",
                "Orders",
                "Customer"
            ],

            "relationships": [
                {
                    "from": "Inventory",
                    "impact": "Order_Fulfillment"
                },
                {
                    "from": "Fleet",
                    "impact": "ETA_Accuracy"
                },
                {
                    "from": "Warehouse",
                    "impact": "OTIF"
                }
            ],

            "learning": {
                "patterns_detected": len(records),
                "status": "UPDATED"
            }
        }

        return graph



if __name__ == "__main__":

    memory = EnterpriseMemory()

    memory.store(
        "Inventory mismatch detected",
        "Inventory Re-Sync",
        "OTIF protected"
    )

    memory.store(
        "Driver ETA unstable",
        "Route Optimization",
        "SLA maintained"
    )


    graph = KnowledgeGraph()

    result = {
        "system": "AEON MATRIX ENTERPRISE MEMORY",
        "status": "ONLINE",

        "memory": {
            "records": memory.retrieve(),
            "count": len(memory.retrieve())
        },

        "knowledge_graph": graph.build(
            memory.retrieve()
        ),

        "continuous_learning": {
            "model_feedback": "CAPTURED",
            "future_prediction": "ENABLED"
        }
    }


    print("=================================")
    print(" AEON MATRIX MEMORY CORE ")
    print("=================================")

    print(json.dumps(result, indent=2))

    print("=================================")
    print(" CONTINUOUS LEARNING ONLINE ")
    print(" Sense > Learn > Improve ")
    print("=================================")
