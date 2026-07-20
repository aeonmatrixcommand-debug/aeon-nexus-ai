from .nodes.node_registry import create_node
from .graph.relationship_graph import create_relationship
from .reasoning.reasoning_engine import reason
from .context.context_analyzer import analyze_context
from .memory.knowledge_memory import save


person = create_node(
    "Warehouse_Manager",
    "PEOPLE"
)

process = create_node(
    "Inventory_Control",
    "PROCESS"
)

relation = create_relationship(
    person,
    process,
    "MANAGES"
)

reasoning = reason(
    relation
)

context = analyze_context(
    "STOCK_OPTIMIZATION"
)

print(person)
print(process)
print(relation)
print(reasoning)
print(context)
print(save(reasoning))
