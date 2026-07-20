from .node.knowledge_node import create
from .graph.relationship_graph import connect
from .retrieval.memory_search import search
from .experience.experience_engine import learn
from .memory.organization_memory import save


node = create(
    "SUPPLY_CHAIN_KNOWLEDGE",
    "OPTIMIZATION_PATTERN"
)

relation = connect(
    "SUPPLY_CHAIN",
    "BUSINESS_VALUE"
)

memory = search(
    "PREVIOUS_OPTIMIZATION_DECISION"
)

experience = learn(
    "OPERATION_EVENT"
)

print(node)
print(relation)
print(memory)
print(experience)
print(save(experience))
