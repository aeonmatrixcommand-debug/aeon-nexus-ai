from .engine.alert_engine import create
from .priority.priority_engine import calculate
from .correlation.signal_correlation import analyze
from .notification.notification_router import route
from .escalation.escalation_engine import escalate
from .memory.alert_memory import save


signal = {
    "event": "INVENTORY_RISK",
    "risk_score": 91,
    "source": "TELEMETRY_HUB"
}


alert = create(signal)

priority = calculate(alert)

correlation = analyze(
    [signal, alert]
)

notification = route(alert)

escalation = escalate(alert)

memory = save(
    {
        "alert": alert,
        "priority": priority,
        "correlation": correlation,
        "notification": notification,
        "escalation": escalation
    }
)


print(alert)
print(priority)
print(correlation)
print(notification)
print(escalation)
print(memory)
