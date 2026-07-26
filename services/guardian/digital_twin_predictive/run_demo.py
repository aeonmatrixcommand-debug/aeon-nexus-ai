from .entity.twin_entity import create_entity
from .simulation.simulation_engine import simulate
from .impact.impact_analyzer import analyze
from .prediction.predictive_engine import predict
from .memory.simulation_memory import save


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
