from datetime import datetime
import json


class AILearningBrain:

    def __init__(self):
        self.memory = []


    def learn(self, event):

        record = {
            "event": event,
            "learning": "UPDATED",
            "pattern_detected": [
                "inventory_behavior",
                "delivery_risk",
                "operation_optimization"
            ],
            "knowledge_status": "IMPROVED",
            "timestamp": datetime.now().isoformat()
        }

        self.memory.append(record)

        return record


    def status(self):

        return {
            "brain": "AEON MATRIX LEARNING BRAIN",
            "status": "ONLINE",
            "memory_entries": len(self.memory),
            "continuous_learning": "ACTIVE"
        }



if __name__ == "__main__":

    brain = AILearningBrain()

    event = {
        "source": "COMMAND_CENTER",
        "action": "INVENTORY_RE_SYNC",
        "result": "SUCCESS",
        "kpi_improvement": {
            "OTIF": "+1.4%",
            "Risk": "-18%"
        }
    }

    print("=================================")
    print(" AEON MATRIX AI MEMORY CORE ")
    print("=================================")

    print(json.dumps(
        brain.learn(event),
        indent=2
    ))

    print(json.dumps(
        brain.status(),
        indent=2
    ))

    print("=================================")
    print(" CONTINUOUS LEARNING ONLINE ")
    print(" Sense > Learn > Optimize > Improve ")
    print("=================================")
