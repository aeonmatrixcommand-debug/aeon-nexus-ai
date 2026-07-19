class Event:
    def __init__(self, source, event_type, payload):
        self.source = source
        self.event_type = event_type
        self.payload = payload

    def to_dict(self):
        return {
            "source": self.source,
            "event_type": self.event_type,
            "payload": self.payload
        }
