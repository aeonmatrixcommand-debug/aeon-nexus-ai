from .monitor.operations_monitor import monitor
from .resource.resource_controller import allocate
from .priority.action_priority import prioritize
from .dashboard.control_dashboard import generate
from .memory.operations_memory import save


operation = monitor(
    "WAREHOUSE_OPERATION"
)

resource = allocate(
    "LOGISTICS_CAPACITY"
)

priority = prioritize(
    [
        "RESTOCK_CRITICAL_SKU",
        "OPTIMIZE_ROUTE"
    ]
)

dashboard = generate(
    [
        operation,
        resource,
        priority
    ]
)

print(operation)
print(resource)
print(priority)
print(dashboard)
print(save(dashboard))
