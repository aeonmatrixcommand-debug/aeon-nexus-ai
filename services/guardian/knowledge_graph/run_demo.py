from .entity.entity_registry import register
from .relationship.relation_engine import connect
from .event.event_builder import create
from .query.intelligence_query import search
from .memory.knowledge_memory import save


entity = register(
    "WAREHOUSE_SYSTEM",
    "OPERATION_PLATFORM"
)

relation = connect(
    "WAREHOUSE_SYSTEM",
    "INVENTORY_DATA",
    "PRODUCES_SIGNAL"
)

event = create(
    "STOCK_RISK_DETECTED"
)

query = search(
    "WHY_INVENTORY_RISK_OCCURRED"
)

print(entity)
print(relation)
print(event)
print(query)
print(save(query))
