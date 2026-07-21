from .value.value_analyzer import analyze_value
from .cost.cost_optimizer import optimize
from .revenue.revenue_detector import detect_opportunity
from .decision.business_decision import create_decision
from .memory.value_memory import save
from .resource.resource_allocator import allocate


value = analyze_value(
    "AUTONOMOUS_ROUTE_OPTIMIZATION"
)

cost = optimize(
    "LOGISTICS_RESOURCE"
)

revenue = detect_opportunity(
    "CUSTOMER_DEMAND_SIGNAL"
)

decision = create_decision(
    value,
    cost,
    revenue
)

print(value)
print(cost)
print(revenue)
print(decision)
print(save(decision))

resource = allocate(
    "AI_AGENT_CAPACITY"
)

print(cost)
print(value)
print(resource)
print(save(value))
