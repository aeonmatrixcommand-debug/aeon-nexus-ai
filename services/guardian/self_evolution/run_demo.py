from .outcome.outcome_collector import collect
from .learning.learning_engine import learn
from .improvement.improvement_core import improve
from .policy.policy_evolution import evolve
from .memory.evolution_memory import save


outcome = collect(
    "OPERATION_RESULT"
)

learning = learn(
    outcome
)

improvement = improve(
    learning
)

policy = evolve(
    improvement
)

print(outcome)
print(learning)
print(improvement)
print(policy)
print(save(policy))
