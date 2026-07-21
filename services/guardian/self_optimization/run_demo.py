from services.guardian.self_optimization.health.system_health import SystemHealthMonitor
from services.guardian.self_optimization.diagnosis.agent_diagnosis import diagnose
from services.guardian.self_optimization.optimization.optimization_loop import optimize
from services.guardian.self_optimization.maintenance.predictive_signal import create_signal
from services.guardian.self_optimization.recovery.self_healing import recommend_recovery


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
