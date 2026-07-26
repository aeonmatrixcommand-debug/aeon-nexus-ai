from datetime import datetime
from datetime import datetime, UTC


class LearningBridge:

    def __init__(self):
        self.events = []

    def record(self, event):
        payload = {
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.events.append(payload)

            "timestamp": datetime.now(UTC).isoformat(),
        }
        self.events.append(payload)
        return payload

    def get_events(self):
        return self.events


def process_outcome(trace_id, action, outcome):
    bridge = LearningBridge()
    return bridge.record(
        {
            "trace_id": trace_id,
            "action": action,
            "outcome": outcome,
        }
    )
