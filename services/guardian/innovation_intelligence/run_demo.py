from .idea.idea_engine import generate
from .experiment.experiment_manager import run
from .evaluation.outcome_evaluator import evaluate
from .learning.feedback_loop import learn
from .memory.innovation_memory import save


idea = generate(
    "WAREHOUSE_AUTOMATION"
)

experiment = run(
    idea
)

outcome = evaluate(
    experiment
)

learning = learn(
    outcome
)

print(idea)
print(experiment)
print(outcome)
print(learning)
print(save(learning))
