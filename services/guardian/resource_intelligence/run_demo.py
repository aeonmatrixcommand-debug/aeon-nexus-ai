from .analyzer.resource_analyzer import analyze
from .allocation.dynamic_allocator import allocate
from .capacity.capacity_optimizer import optimize
from .cost.cost_planner import plan
from .memory.resource_memory import save


resource = analyze(
    "LOGISTICS_RESOURCES"
)

allocation = allocate(
    resource
)

capacity = optimize(
    "WAREHOUSE_CAPACITY"
)

cost = plan(
    "OPERATION_COST"
)

print(resource)
print(allocation)
print(capacity)
print(cost)
print(save(allocation))
