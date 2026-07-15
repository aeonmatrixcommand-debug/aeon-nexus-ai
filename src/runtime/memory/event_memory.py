class EventMemory:
    """
    Store operational events for autonomous learning.
    """

    def __init__(self):
        self.events = []


    def record(self, event):

        self.events.append(event)

        return {
            "stored": True,
            "event_count": len(self.events)
        }


    def recent(self):

        return self.events[-10:]
