<<<<<<< HEAD
from .state.twin_state import create_state
from .simulation.simulation_engine import simulate_change
from .governance.governance_check import validate
from .impact.impact_engine import analyze
from .memory.twin_memory import save
=======
from services.guardian.digital_twin_governance.state.twin_state import create_state
from services.guardian.digital_twin_governance.simulation.simulation_engine import simulate_change
from services.guardian.digital_twin_governance.governance.governance_check import validate
from services.guardian.digital_twin_governance.impact.impact_engine import analyze
from services.guardian.digital_twin_governance.memory.twin_memory import save
>>>>>>> origin/main


state = create_state(
    "AEON WMS",
    {
        "inventory_accuracy": 96,
        "service_level": 98
    }
)

simulation = simulate_change(
    state,
    "OPTIMIZE_ROUTE_ALLOCATION"
)

governance = validate(simulation)

impact = analyze(simulation)

print(state)
print(simulation)
print(governance)
print(impact)
print(save(impact))
