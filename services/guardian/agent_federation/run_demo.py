from .registry.agent_registry import register
from .communication.message_bus import send
from .coordination.coordinator import coordinate
from .monitor.agent_monitor import monitor
from .memory.agent_memory import save


guardian = register(
    "GUARDIAN_AI",
    "GOVERNANCE"
)

forecast = register(
    "FORECAST_AGENT",
    "PREDICTION"
)

message = send(
    "FORECAST_AGENT",
    "GUARDIAN_AI",
    "DEMAND_RISK_SIGNAL"
)

coordination = coordinate(
    [
        guardian,
        forecast
    ],
    "OPTIMIZE_INVENTORY_DECISION"
)

performance = monitor(
    guardian
)

print(guardian)
print(forecast)
print(message)
print(coordination)
print(performance)
print(save(coordination))
