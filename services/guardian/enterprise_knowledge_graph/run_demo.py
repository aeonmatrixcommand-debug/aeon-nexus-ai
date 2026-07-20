from .entity.entity_manager import create
from .graph.relationship_graph import connect
from .reasoning.reasoning_engine import reason
from .query.knowledge_query import query
from .memory.knowledge_memory import save


warehouse = create(
    "WAREHOUSE_A",
    "LOGISTICS_NODE"
)

inventory = create(
    "INVENTORY_SYSTEM",
    "BUSINESS_SYSTEM"
)

relationship = connect(
    warehouse,
    inventory,
    "DEPENDS_ON"
)

reasoning = reason(
    relationship
)

answer = query(
    "WHY_INVENTORY_RISK_INCREASED"
)

print(warehouse)
print(inventory)
print(relationship)
print(reasoning)
print(answer)
print(save(reasoning))
