class EventBus:
    def publish(self, event):
        return {"status": "published", "event": event}

    def health(self):
        return {"service":"event_bus","status":"healthy"}
