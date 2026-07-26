<<<<<<< HEAD
from .entity.twin_entity import create_entity
from .simulation.simulation_engine import simulate
from .impact.impact_analyzer import analyze
from .prediction.predictive_engine import predict
from .memory.simulation_memory import save
=======
from services.guardian.digital_twin_predictive.entity.twin_entity import create_entity
from services.guardian.digital_twin_predictive.simulation.simulation_engine import simulate
from services.guardian.digital_twin_predictive.impact.impact_analyzer import analyze
from services.guardian.digital_twin_predictive.prediction.predictive_engine import predict
from services.guardian.digital_twin_predictive.memory.simulation_memory import save
>>>>>>> origin/main


warehouse = create_entity(
    "MAIN_WAREHOUSE",
    "LOGISTICS_NODE"
)

simulation = simulate(
    warehouse,
    "DEMAND_SPIKE"
)

impact = analyze(
    simulation
)

prediction = predict(
    impact
)

print(warehouse)
print(simulation)
print(impact)
print(prediction)
print(save(prediction))
