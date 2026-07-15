from dataclasses import dataclass


@dataclass
class AgentMessage:

    sender: str
    receiver: str
    message_type: str
    payload: dict

