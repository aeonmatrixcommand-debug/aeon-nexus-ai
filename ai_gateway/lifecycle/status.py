from enum import Enum


class AgentStatus(Enum):

    CREATED = "CREATED"
    INITIALIZING = "INITIALIZING"
    READY = "READY"
    RUNNING = "RUNNING"
    LEARNING = "LEARNING"
    PAUSED = "PAUSED"
    FAILED = "FAILED"
    RECOVERED = "RECOVERED"
