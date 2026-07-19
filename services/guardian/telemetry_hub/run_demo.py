from .collector.event_collector import collect
from .processor.signal_processor import process
from .router.event_router import route
from .alert.cognitive_alert import generate
from .memory.telemetry_memory import save


event = collect(
    "INVENTORY_RISK_EVENT"
)

signal = process(
    event
)

routing = route(
    signal
)

alert = generate(
    routing
)

print(event)
print(signal)
print(routing)
print(alert)
print(save(alert))
