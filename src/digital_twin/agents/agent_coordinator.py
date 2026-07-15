class AgentCoordinator:
    """
    Coordinate multiple AI agents.
    """

    def coordinate(self, task):

        agents = [
            "risk_agent",
            "impact_agent",
            "decision_agent"
        ]

        return {
            "task": task,
            "agents": agents,
            "status": "coordinated"
        }
