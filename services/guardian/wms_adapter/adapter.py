class WMSAdapter:

    def transform(self, event: dict) -> dict:
        return {
            "source": "wms",
            "event_type": event.get("event_type"),
            "warehouse": event.get("warehouse"),
            "timestamp": event.get("timestamp"),
            "payload": event,
        }
