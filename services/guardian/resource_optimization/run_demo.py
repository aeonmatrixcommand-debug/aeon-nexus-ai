from .registry.resource_registry import register
from .capacity.capacity_analyzer import analyze
from .allocation.allocation_engine import allocate
from .monitor.utilization_monitor import monitor
from .memory.resource_memory import save


resource = register(
    "WAREHOUSE_CAPACITY",
    "LOGISTICS_RESOURCE"
)

capacity = analyze(
    resource
)

allocation = allocate(
    resource,
    "HIGH_DEMAND_PERIOD"
)

utilization = monitor(
    allocation
)

print(resource)
print(capacity)
print(allocation)
print(utilization)
print(save(utilization))
