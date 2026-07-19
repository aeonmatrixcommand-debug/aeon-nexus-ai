from .avatar.avatar_core import create_avatar
from .knowledge.knowledge_navigator import search_knowledge
from .sop.sop_assistant import explain_sop
from .learning.learning_companion import recommend_learning
from .memory.avatar_memory import save_interaction


avatar = create_avatar(
    "AEON Assistant",
    "Enterprise Knowledge Companion"
)

knowledge = search_knowledge(
    "Inventory SOP"
)

sop = explain_sop(
    "Warehouse Operation"
)

learning = recommend_learning(
    "AI Workflow"
)

print(avatar)
print(knowledge)
print(sop)
print(learning)
print(save_interaction(avatar))
