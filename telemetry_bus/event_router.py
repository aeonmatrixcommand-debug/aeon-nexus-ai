from telemetry_bus.event_processor import EventProcessor

class EventRouter:

    def __init__(self):
        self.processor = EventProcessor()

    def route(self, event):
        return self.processor.process(event)
