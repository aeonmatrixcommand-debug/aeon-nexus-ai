class EventBus:

    def publish(self,event):
        return {
            "event": event,
            "published": True
        }

    def consume(self,event):
        return {
            "event": event,
            "consumed": True
        }
