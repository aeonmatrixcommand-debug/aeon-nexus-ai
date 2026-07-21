<<<<<<< HEAD
from .model.twin_model import create
from .scenario.scenario_engine import simulate
from .impact.impact_analyzer import analyze
from .prediction.future_predictor import predict
from .memory.simulation_memory import save
=======
from services.guardian.digital_twin_simulation.model.twin_model import create
from services.guardian.digital_twin_simulation.scenario.scenario_engine import simulate
from services.guardian.digital_twin_simulation.impact.impact_analyzer import analyze
from services.guardian.digital_twin_simulation.prediction.future_predictor import predict
from services.guardian.digital_twin_simulation.memory.simulation_memory import save
>>>>>>> 1df4713 (fix: migrate guardian imports to services namespace)


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
