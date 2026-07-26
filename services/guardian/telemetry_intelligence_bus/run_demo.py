from .event.event_bus import publish
from .collector.signal_collector import collect
from .analysis.signal_analyzer import analyze
from .monitor.health_monitor import check
from .memory.telemetry_memory import save


event = publish(
    "INVENTORY_UPDATED"
)

signal = collect(
    "WMS",
    "STOCK_LEVEL"
)

analysis = analyze(
    signal
)

health = check(
    "AEON_MATRIX_CORE"
)

print(event)
print(signal)
print(analysis)
print(health)
print(save(health))
