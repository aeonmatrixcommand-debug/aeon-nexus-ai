"""
AEON MATRIX Multi-Agent Coordinator
Sprint 86
"""


from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class AgentTask:
    agent: str
    task: str
    priority: str
    timestamp: str


class AgentCoordinator:

    def assign(
        self,
        agent,
        task,
        priority,
    ):

        return AgentTask(
            agent=agent,
            task=task,
            priority=priority,
            timestamp=datetime.now(UTC).isoformat(),
        )
