from .core.os_core import initialize
from .registry.service_registry import register
from .bus.ai_message_bus import publish
from .monitor.system_monitor import check
from .memory.os_memory import save


system = initialize(
    "AEON_MATRIX_ENTERPRISE_OS"
)

service = register(
    "GUARDIAN_AI_SERVICE"
)

event = publish(
    "AUTONOMOUS_DECISION_EVENT"
)

health = check()

print(system)
print(service)
print(event)
print(health)
print(save(health))
