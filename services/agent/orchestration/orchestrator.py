from dataclasses import dataclass, field


@dataclass
class AgentTask:
    agent_id: str
    intent: str
    payload: dict


class AgentOrchestrator:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent_id: str):
        self.agents[agent_id] = True

    def dispatch(self, task: AgentTask):
        if task.agent_id not in self.agents:
            raise ValueError("Agent not registered")

        return {
            "agent_id": task.agent_id,
            "status": "accepted",
            "intent": task.intent,
            "payload": task.payload,
        }
