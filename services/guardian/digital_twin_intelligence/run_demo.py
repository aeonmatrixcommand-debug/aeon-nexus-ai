<<<<<<< HEAD
from .model.twin_model import create
from .simulation.scenario_simulator import simulate
from .prediction.impact_predictor import predict
from .evaluation.simulation_evaluator import evaluate
from .memory.twin_memory import save
=======
from services.guardian.digital_twin_intelligence.model.twin_model import create
from services.guardian.digital_twin_intelligence.simulation.scenario_simulator import simulate
from services.guardian.digital_twin_intelligence.prediction.impact_predictor import predict
from services.guardian.digital_twin_intelligence.evaluation.simulation_evaluator import evaluate
from services.guardian.digital_twin_intelligence.memory.twin_memory import save
>>>>>>> origin/main


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
