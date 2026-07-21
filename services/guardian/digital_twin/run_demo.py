<<<<<<< HEAD
from .model.twin_model import create
from .scenario.scenario_engine import generate
from .simulation.simulation_engine import run
from .analysis.impact_analyzer import analyze
from .memory.simulation_memory import save
=======
from services.guardian.digital_twin.model.twin_model import create
from services.guardian.digital_twin.scenario.scenario_engine import generate
from services.guardian.digital_twin.simulation.simulation_engine import run
from services.guardian.digital_twin.analysis.impact_analyzer import analyze
from services.guardian.digital_twin.memory.simulation_memory import save
>>>>>>> 1df4713 (fix: migrate guardian imports to services namespace)


twin = create(
    "AEON_WAREHOUSE_OPERATION"
)


scenario = generate(
    {
        "event": "STOCK_SHORTAGE",
        "risk": 85
    }
)


simulation = run(
    scenario
)


impact = analyze(
    simulation
)


memory = save(
    {
        "twin": twin,
        "scenario": scenario,
        "simulation": simulation,
        "impact": impact
    }
)


print(twin)
print(scenario)
print(simulation)
print(impact)
print(memory)
