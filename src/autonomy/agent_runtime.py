from digital_twin.agents.agent_coordinator import AgentCoordinator
from digital_twin.agents.agent_guard import AgentGuard


class AgentRuntime:
    """
    Execute coordinated AI agents.
    """

    def __init__(self):

        self.coordinator = AgentCoordinator()
        self.guard = AgentGuard()


    def run(self, task):

        agents = self.coordinator.coordinate(task)

        validation = self.guard.validate(task)

        return {
            "agents": agents,
            "validation": validation,
            "status": "ready"
        }
