from .health.system_health import SystemHealthMonitor
from .diagnosis.agent_diagnosis import diagnose
from .optimization.optimization_loop import optimize
from .maintenance.predictive_signal import create_signal
from .recovery.self_healing import recommend_recovery


health = SystemHealthMonitor().check(
    {
        "score": 86
    }
)

agent_issue = diagnose(
    {
        "name": "Forecast Agent",
        "accuracy": 87,
        "latency": 600
    }
)

print(health)
print(agent_issue)

for issue in agent_issue["issues"]:
    print(optimize(issue))

print(
    create_signal(
        "AEON MATRIX CORE"
    )
)

print(
    recommend_recovery(
        health["status"]
    )
)
