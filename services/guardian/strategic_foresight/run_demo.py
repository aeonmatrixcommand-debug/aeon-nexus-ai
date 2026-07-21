<<<<<<< HEAD
from .signal.world_signal import collect_signal
from .risk.risk_forecast import forecast
from .scenario.scenario_engine import simulate
from .simulation.strategy_simulator import evaluate_strategy
from .memory.foresight_memory import save_prediction
=======
from services.guardian.strategic_foresight.signal.world_signal import collect_signal
from services.guardian.strategic_foresight.risk.risk_forecast import forecast
from services.guardian.strategic_foresight.scenario.scenario_engine import simulate
from services.guardian.strategic_foresight.simulation.strategy_simulator import evaluate_strategy
from services.guardian.strategic_foresight.memory.foresight_memory import save_prediction
>>>>>>> 1df4713 (fix: migrate guardian imports to services namespace)


signal = collect_signal(
    "SUPPLY_CHAIN_PRESSURE",
    91
)

risk = forecast(signal)

scenario = simulate(
    "GLOBAL_SUPPLY_DISRUPTION",
    risk
)

strategy = evaluate_strategy(
    scenario
)

memory = save_prediction(
    strategy
)

print(signal)
print(risk)
print(scenario)
print(strategy)
print(memory)
