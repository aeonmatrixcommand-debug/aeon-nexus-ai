from .model.twin_model import create
from .simulation.scenario_simulator import simulate
from .prediction.impact_predictor import predict
from .evaluation.simulation_evaluator import evaluate
from .memory.twin_memory import save


twin = create(
    "ENTERPRISE_OPERATION_MODEL"
)

simulation = simulate(
    "SUPPLY_CHAIN_OPTIMIZATION"
)

prediction = predict(
    simulation
)

evaluation = evaluate(
    prediction
)

print(twin)
print(simulation)
print(prediction)
print(evaluation)
print(save(evaluation))
