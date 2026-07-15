from telemetry.event_bus import EventBus
from telemetry.audit_logger import AuditLogger
from telemetry.metric_collector import MetricCollector


class SystemOrchestrator:
    """
    AEON MATRIX Enterprise Runtime Orchestrator.
    """

    def __init__(self):

        self.events = EventBus()
        self.audit = AuditLogger()
        self.metrics = MetricCollector()


    def health(self):

        return self.metrics.collect()


    def process(self, event):

        self.events.publish(event)

        result = {
            "event": event,
            "status": "received"
        }

        self.audit.log(
            "runtime_event",
            result
        )

        return result


if __name__ == "__main__":

    runtime = SystemOrchestrator()

    print(
        "=================================================="
    )

    print(
        "[ AEON MATRIX // RUNTIME ORCHESTRATOR ]"
    )

    print(
        "=================================================="
    )

    print(
        "Health:",
        runtime.health()
    )

    print(
        "Process:",
        runtime.process(
            {
                "type": "warehouse_event",
                "source": "DC01",
                "signal": "temperature_warning"
            }
        )
    )
