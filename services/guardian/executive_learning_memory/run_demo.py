from .capture.experience_capture import capture
from .outcome.outcome_learning import learn
from .knowledge.knowledge_builder import consolidate
from .insight.executive_insight import generate
from .memory.organizational_memory import save


experience = capture(
    "INVENTORY_OPTIMIZATION_DECISION"
)

learning = learn(
    "WASTE_REDUCTION_SUCCESS"
)

knowledge = consolidate(
    [
        experience,
        learning
    ]
)

insight = generate(
    knowledge
)

print(experience)
print(learning)
print(knowledge)
print(insight)
print(save(insight))
