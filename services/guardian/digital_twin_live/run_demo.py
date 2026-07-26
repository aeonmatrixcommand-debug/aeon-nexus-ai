from .state.twin_state import update
from .sync.live_sync import synchronize
from .simulation.live_simulator import simulate
from .impact.live_impact import analyze
from .memory.twin_memory import save


state = update(
    "AEON_WAREHOUSE",
    "OPERATIONAL"
)

sync = synchronize(
    "INVENTORY_TELEMETRY"
)

simulation = simulate(
    "DEMAND_SPIKE_25_PERCENT"
)

impact = analyze(
    simulation
)

print(state)
print(sync)
print(simulation)
print(impact)
print(save(impact))
