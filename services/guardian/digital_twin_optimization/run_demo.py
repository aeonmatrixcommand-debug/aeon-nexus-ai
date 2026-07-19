from .fusion.intelligence_fusion import fuse
from .optimizer.future_optimizer import optimize
from .scenario.scenario_ranker import rank
from .planner.optimization_planner import plan
from .memory.optimization_memory import save


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
