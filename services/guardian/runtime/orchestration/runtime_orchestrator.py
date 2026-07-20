from services.guardian.runtime.agents.coordinator import AgentCoordinator
from services.guardian.runtime.learning_bridge import LearningBridge


class RuntimeOrchestrator:

    def __init__(self):
        self.coordinator = AgentCoordinator()
        self.learning = LearningBridge()

    def execute(self, task):
        result = self.coordinator.assign(task)

        self.learning.record(
            {
                "task": task,
                "result": result
            }
        )

        return result
