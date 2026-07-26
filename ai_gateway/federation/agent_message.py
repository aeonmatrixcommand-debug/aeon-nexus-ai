from datetime import datetime


class AgentMessage:


    def __init__(
        self,
        sender,
        receiver,
        message_type,
        payload
    ):

        self.sender = sender
        self.receiver = receiver
        self.message_type = message_type
        self.payload = payload
        self.timestamp = datetime.utcnow().isoformat()



    def to_dict(self):

        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "type": self.message_type,
            "payload": self.payload,
            "timestamp": self.timestamp
        }
