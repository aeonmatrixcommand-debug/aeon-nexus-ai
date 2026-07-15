class EventStream:
    """
    Real-time enterprise event stream.
    """

    def __init__(self):
        self.events = []


    def publish(self, event):

        self.events.append(event)

        return {
            "event": event,
            "stream_status": "published"
        }


    def latest(self):

        return self.events[-10:]
