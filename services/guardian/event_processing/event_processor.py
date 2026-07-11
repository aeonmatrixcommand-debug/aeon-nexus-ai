class EventProcessor:
    def process(self, event: dict) -> dict:
        return {
            "event_type": event.get("type"),
            "status": "processed",
            "payload": event,
        }
