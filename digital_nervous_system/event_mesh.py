import json
from datetime import datetime
from pathlib import Path


class EventRegistry:

    def __init__(self):
        self.events = []


    def publish(self, source, event_type, payload):

        event = {
            "event_id":
                f"EVT-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",

            "source":
                source,

            "event_type":
                event_type,

            "payload":
                payload,

            "timestamp":
                datetime.utcnow().isoformat()
        }

        self.events.append(event)

        return event


    def stream(self):

        return {
            "stream_status": "ACTIVE",
            "events": self.events
        }


class DigitalNervousSystem:

    def __init__(self):
        self.registry = EventRegistry()


    def ingest(self, telemetry):

        event = self.registry.publish(
            source=telemetry.get("source"),
            event_type=telemetry.get("type"),
            payload=telemetry.get("data")
        )

        return event


if __name__ == "__main__":

    nervous_system = DigitalNervousSystem()

    event = nervous_system.ingest(
        {
            "source": "WMS",
            "type": "INVENTORY_ALERT",
            "data": {
                "sku": "SKU-CRITICAL",
                "risk": "HIGH",
                "action": "RE_SYNC_REQUIRED"
            }
        }
    )


    print("=" * 60)
    print(" AEON MATRIX DIGITAL NERVOUS SYSTEM")
    print("=" * 60)

    print(json.dumps(
        {
            "event": event,
            "stream":
                nervous_system.registry.stream()
        },
        indent=2
    ))
