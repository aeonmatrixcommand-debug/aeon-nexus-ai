from .pool.resource_pool import AgentResourcePool
from .matching.capability_matcher import match_agent
from .allocation.task_allocator import TaskAllocator
from .optimization.resource_optimizer import optimize
from .audit.allocation_audit import log_allocation


pool = AgentResourcePool()

pool.register(
    "Forecast Agent",
    "DEMAND_FORECAST",
    80
)

pool.register(
    "Insight Agent",
    "BUSINESS_ANALYSIS",
    70
)


agent = match_agent(
    "DEMAND_FORECAST",
    pool.agents
)


allocation = TaskAllocator().allocate(
    "Demand Prediction",
    agent
)

print(allocation)
print(optimize(agent))
print(log_allocation(allocation))
