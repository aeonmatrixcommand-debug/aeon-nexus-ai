from datetime import datetime
import json
import uuid


class TelemetryTower:

    def __init__(self):
        self.events = []


    def publish(self, source, event_type, payload):

        event = {
            "event_id": str(uuid.uuid4()),
            "source": source,
            "event_type": event_type,
            "payload": payload,
            "timestamp": datetime.now().isoformat()
        }

        self.events.append(event)

        return event


    def monitor(self):

        return {
            "tower_status": "ONLINE",
            "stream_status": "ACTIVE",
            "events_received": len(self.events),
            "last_event": self.events[-1] if self.events else None
        }



if __name__ == "__main__":

    tower = TelemetryTower()

    print("=================================")
    print(" AEON MATRIX TELEMETRY TOWER ")
    print("=================================")

    tower.publish(
        "WMS",
        "WAREHOUSE_ALERT",
        {
            "inventory": "MISMATCH_DETECTED",
            "order": "DELAY_INCREASING",
            "driver": "ETA_UNSTABLE"
        }
    )

    tower.publish(
        "TMS",
        "FLEET_STATUS",
        {
            "route": "OPTIMIZATION_REQUIRED",
            "risk": "MONITORING"
        }
    )

    print(json.dumps(
        tower.monitor(),
        indent=2
    ))

    print("=================================")
    print(" REAL-TIME TELEMETRY ONLINE ")
    print(" Sense > Stream > Analyze > Act ")
    print("=================================")
