from .registry.knowledge_registry import KnowledgeRegistry
from .memory.sop_memory import SOPMemory
from .memory.lessons_learned import LessonsLearned
from .retrieval.knowledge_search import search_knowledge


registry = KnowledgeRegistry()

knowledge = registry.register(
    "Inventory Risk Response",
    "Operations",
    "Verify stock, analyze demand, request approval"
)

sop = SOPMemory().store(
    "Inventory Adjustment",
    "Human approval required for high risk"
)

lesson = LessonsLearned().capture(
    "Stock Shortage Event",
    "Early detection reduces operational impact"
)

records = [
    knowledge,
    sop,
    lesson
]

print(search_knowledge(records, "risk"))
