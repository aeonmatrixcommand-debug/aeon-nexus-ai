import json
from pathlib import Path
from datetime import datetime


class AgentMemoryStore:

    def __init__(self, path="agent_learning_memory/memory.json"):
        self.path = Path(path)
        self.path.parent.mkdir(
            exist_ok=True
        )

        if not self.path.exists():
            self.path.write_text("[]")


    def save(self, experience):

        memories = json.loads(
            self.path.read_text()
        )

        memories.append(experience)

        self.path.write_text(
            json.dumps(
                memories,
                indent=2
            )
        )


    def recall(self):

        return json.loads(
            self.path.read_text()
        )


class ContinuousLearningEngine:

    def __init__(self):
        self.memory = AgentMemoryStore()


    def learn(self, event, decision, outcome):

        experience = {

            "memory_id":
                f"MEM-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",

            "event":
                event,

            "decision":
                decision,

            "outcome":
                outcome,

            "learning":
                "Improve future decision confidence",

            "timestamp":
                datetime.utcnow().isoformat()
        }

        self.memory.save(experience)

        return experience


if __name__ == "__main__":

    engine = ContinuousLearningEngine()

    result = engine.learn(
        {
            "system": "AEON MATRIX",
            "incident": "Inventory Risk Detection"
        },

        {
            "action": "INVENTORY_RE_SYNC",
            "agent": "Decision Agent"
        },

        {
            "status": "RECOVERED",
            "kpi": {
                "OTIF": "RESTORED"
            }
        }
    )


    print("=" * 55)
    print(" AEON MATRIX CONTINUOUS LEARNING")
    print("=" * 55)

    print(json.dumps(
        result,
        indent=2
    ))
