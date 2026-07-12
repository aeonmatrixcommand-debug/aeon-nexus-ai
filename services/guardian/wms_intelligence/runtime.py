class WMSIntelligence:

    def process_event(self, event):
        event_type = event.get("type", "")

        return {
            "event": event_type,
            "validated": True
        }
