<<<<<<< HEAD
from .event.event_bus import publish
from .collector.signal_collector import collect
from .analysis.signal_analyzer import analyze
from .monitor.health_monitor import check
from .memory.telemetry_memory import save
=======
from services.guardian.telemetry_intelligence_bus.event.event_bus import publish
from services.guardian.telemetry_intelligence_bus.collector.signal_collector import collect
from services.guardian.telemetry_intelligence_bus.analysis.signal_analyzer import analyze
from services.guardian.telemetry_intelligence_bus.monitor.health_monitor import check
from services.guardian.telemetry_intelligence_bus.memory.telemetry_memory import save
>>>>>>> origin/main


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
