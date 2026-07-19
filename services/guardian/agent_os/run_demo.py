from .lifecycle.agent_lifecycle import AgentLifecycle
from .health.agent_health import check_health
from .permission.permission_control import grant_permission
from .tasks.task_registry import TaskRegistry
from .evaluation.performance_score import evaluate


agent = AgentLifecycle().create(
    "Forecast Agent",
    "Demand Intelligence"
)

print(check_health(agent))

print(
    grant_permission(
        agent["agent"],
        "ANALYZE_DEMAND"
    )
)

tasks = TaskRegistry()

print(
    tasks.assign(
        agent["agent"],
        "Forecast next demand cycle"
    )
)

print(
    evaluate(
        agent["agent"],
        95,
        92
    )
)
