class EventBus:
    def publish(self, event: dict) -> dict:
        return {
            "event_status": "published",
            "event": event
        }
