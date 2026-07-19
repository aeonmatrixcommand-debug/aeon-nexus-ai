from .evaluation.performance_evaluator import evaluate
from .learning.feedback_loop import learn
from .improvement.improvement_planner import plan
from .controller.evolution_controller import execute
from .memory.evolution_memory import save


evaluation = evaluate(
    "INVENTORY_DECISION_RESULT"
)

learning = learn(
    evaluation
)

improvement = plan(
    learning
)

evolution = execute(
    improvement
)

print(evaluation)
print(learning)
print(improvement)
print(evolution)
print(save(evolution))
