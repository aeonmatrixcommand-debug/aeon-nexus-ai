from services.guardian.digital_twin_optimization.fusion.intelligence_fusion import fuse
from services.guardian.digital_twin_optimization.optimizer.future_optimizer import optimize
from services.guardian.digital_twin_optimization.scenario.scenario_ranker import rank
from services.guardian.digital_twin_optimization.planner.optimization_planner import plan
from services.guardian.digital_twin_optimization.memory.optimization_memory import save


fusion = fuse(
    [
        "TELEMETRY_SIGNAL",
        "FORECAST_SIGNAL",
        "ECONOMIC_SIGNAL"
    ]
)

future = optimize(
    fusion
)

scenario = rank(
    [
        "OPTIMAL_INVENTORY",
        "NORMAL_OPERATION"
    ]
)

action = plan(
    future
)

print(fusion)
print(future)
print(scenario)
print(action)
print(save(action))
