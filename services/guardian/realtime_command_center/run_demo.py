from .telemetry.telemetry_collector import collect
from .event.event_processor import process
from .status.status_engine import monitor
from .decision.decision_router import route
from .memory.live_memory import save


telemetry = collect(
    "ENTERPRISE_TELEMETRY_BUS"
)

event = process(
    "OPERATION_EVENT"
)

status = monitor(
    [
        telemetry,
        event
    ]
)

decision = route(
    status
)

print(telemetry)
print(event)
print(status)
print(decision)
print(save(decision))
