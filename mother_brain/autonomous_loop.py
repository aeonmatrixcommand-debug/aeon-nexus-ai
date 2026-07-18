from telemetry_bus.event_schema import Event
from telemetry_bus.event_router import EventRouter
from mother_brain.decision import DecisionEngine
from guardian.audit import AuditLogger


class AutonomousLoop:

    def __init__(self):
        self.router = EventRouter()
        self.decision = DecisionEngine()
        self.audit = AuditLogger()

    def run(self, event):

        intelligence = self.router.route(event)

        action = "Inventory Re-Sync"

        decision = self.decision.process(action)

        record = self.audit.log(
            action,
            decision
        )

        return {
            "intelligence": intelligence,
            "decision": decision,
            "audit": record
        }


if __name__ == "__main__":

    event = Event(
        "WMS",
        "WAREHOUSE_ALERT",
        """
        Inventory mismatch detected
        Order delay increasing
        Driver ETA unstable
        """
    )

    result = AutonomousLoop().run(event)

    print("\n=== AEON MATRIX AUTONOMOUS LOOP ===")
    print(result)
