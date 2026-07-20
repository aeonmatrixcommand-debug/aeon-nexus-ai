from .shelf_life.shelf_monitor import monitor
from .demand.demand_forecast import forecast
from .waste.waste_predictor import predict
from .recovery.recovery_optimizer import optimize
from .memory.circular_memory import save


shelf = monitor(
    "SKU_FRESH_FOOD",
    2
)

demand = forecast(
    "SKU_FRESH_FOOD"
)

waste = predict(
    500
)

recovery = optimize(
    shelf
)

print(shelf)
print(demand)
print(waste)
print(recovery)
print(save(recovery))
