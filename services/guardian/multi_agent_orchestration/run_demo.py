from .registry.agent_registry import register
from .coordinator.agent_coordinator import coordinate
from .dispatcher.task_dispatcher import dispatch
from .monitor.agent_monitor import monitor
from .memory.agent_memory import save


agents = [
    register("GUARDIAN_AI", "GOVERNANCE"),
    register("FORECAST_AGENT", "PREDICTION"),
    register("DATA_AGENT", "INTELLIGENCE"),
    register("INSIGHT_AGENT", "ANALYSIS")
]

coordination = coordinate(
    agents
)

task = dispatch(
    "OPTIMIZE_ENTERPRISE_OPERATION"
)

health = monitor(
    agents
)

print(agents)
print(coordination)
print(task)
print(health)
print(save(task))
