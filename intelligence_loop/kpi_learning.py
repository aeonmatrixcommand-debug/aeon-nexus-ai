from datetime import datetime
import json


class KPILearningEngine:

    def __init__(self):
        self.memory = []


    def evaluate(self, execution):

        kpi = {
            "OTIF": "98.2%",
            "SLA": "99.1%",
            "Inventory_Accuracy": "99.6%",
            "Productivity": "96.3%",
            "Risk_Score": "LOW",
            "Logistics_Flow_Index": "94.7",
            "execution": execution,
            "learning_status": "UPDATED",
            "timestamp": datetime.now().isoformat()
        }

        self.memory.append(kpi)

        return kpi


if __name__ == "__main__":

    engine = KPILearningEngine()

    execution = {
        "action": "DIVERT_PRIORITY_ORDER_TO_DC_ALPHA",
        "status": "EXECUTED",
        "digital_twin": "SYNCED"
    }

    result = engine.evaluate(execution)

    print("=================================")
    print(" AEON MATRIX KPI INTELLIGENCE ")
    print("=================================")

    print(json.dumps(result, indent=2))

    print("\nLEARNING MEMORY")
    print(json.dumps(engine.memory, indent=2))

    print("=================================")
    print(" CONTINUOUS LEARNING ONLINE ")
    print(" Sense > Act > Measure > Improve ")
    print("=================================")
