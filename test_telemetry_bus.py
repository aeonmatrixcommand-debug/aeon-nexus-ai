from telemetry_bus.event_schema import Event
from telemetry_bus.event_router import EventRouter

event = Event(
    "WMS",
    "WAREHOUSE_ALERT",
    """
    Inventory mismatch detected
    Order delay increasing
    Driver ETA unstable
    """
)

result = EventRouter().route(event)

print(result)
