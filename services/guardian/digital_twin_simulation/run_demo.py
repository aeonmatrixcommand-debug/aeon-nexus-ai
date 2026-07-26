from .model.twin_model import create
from .scenario.scenario_engine import simulate
from .impact.impact_analyzer import analyze
from .prediction.future_predictor import predict
from .memory.simulation_memory import save


twin = create(
    "AEON_WAREHOUSE_OPERATION"
)

scenario = simulate(
    "DEMAND_INCREASE_30_PERCENT"
)

impact = analyze(
    scenario
)

prediction = predict(
    impact
)

print(twin)
print(scenario)
print(impact)
print(prediction)
print(save(prediction))
