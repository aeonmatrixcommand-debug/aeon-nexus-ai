import json
from datetime import datetime


class EnterpriseMemory:


    def __init__(self):

        self.events = []


    def store(self,event):

        self.events.append(event)

        return {

            "memory_id":
                len(self.events),

            "stored":
                True
        }



class KnowledgeGraph:


    def connect(self,event):

        tags=[]


        text = event.lower()


        if "inventory" in text:
            tags.append("INVENTORY_INTELLIGENCE")


        if "delay" in text:
            tags.append("DELIVERY_RISK")


        if "temperature" in text:
            tags.append("SYSTEM_HEALTH")


        return {

            "entity":
                event,

            "relations":
                tags

        }



class ExperienceLearning:


    def analyze(self,graph):

        recommendations=[]


        if "INVENTORY_INTELLIGENCE" in graph["relations"]:

            recommendations.append(
                "Run inventory reconciliation"
            )


        if "DELIVERY_RISK" in graph["relations"]:

            recommendations.append(
                "Optimize ETA prediction"
            )


        if "SYSTEM_HEALTH" in graph["relations"]:

            recommendations.append(
                "Activate preventive monitoring"
            )


        return {

            "learned_patterns":
                graph["relations"],

            "recommendations":
                recommendations,

            "confidence":
                95

        }



class EnterpriseBrain:


    def run(self,event):

        memory = EnterpriseMemory()

        saved = memory.store(event)


        graph = KnowledgeGraph().connect(
            event
        )


        learning = ExperienceLearning().analyze(
            graph
        )


        return {

            "system":
                "AEON MATRIX KNOWLEDGE BRAIN",

            "timestamp":
                datetime.utcnow().isoformat(),

            "memory":
                saved,

            "knowledge_graph":
                graph,

            "learning":
                learning

        }



if __name__=="__main__":


    event = (
        "Warehouse inventory mismatch "
        "causing delivery delay"
    )


    print("="*75)

    print(
        " AEON MATRIX ENTERPRISE MEMORY BRAIN "
    )

    print("="*75)


    print(
        json.dumps(
            EnterpriseBrain().run(event),
            indent=2
        )
    )

