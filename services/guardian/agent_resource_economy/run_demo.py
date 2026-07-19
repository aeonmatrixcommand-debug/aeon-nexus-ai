from .registry.agent_registry import register
from .compute.compute_allocator import allocate_compute
from .scheduler.priority_scheduler import schedule
from .budget.budget_controller import check_budget
from .memory.resource_memory import save


agent = register(
    "Forecast_Agent",
    "Demand Prediction"
)

compute = allocate_compute(
    agent["agent"],
    "HIGH"
)

task = schedule(
    "INVENTORY_OPTIMIZATION",
    "CRITICAL"
)

budget = check_budget(
    72
)

print(agent)
print(compute)
print(task)
print(budget)
print(save(task))
