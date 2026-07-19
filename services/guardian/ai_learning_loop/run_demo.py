from .decision.decision_tracker import record_decision
from .outcome.outcome_engine import evaluate_outcome
from .feedback.feedback_loop import learn_from_feedback
from .strategy.strategy_engine import improve_strategy
from .memory.executive_memory import save_learning


decision = record_decision(
    "Inventory Optimization",
    "TRANSFER_STOCK"
)

outcome = evaluate_outcome(
    decision["decision"],
    92
)

feedback = learn_from_feedback(
    outcome
)

strategy = improve_strategy(
    feedback
)

memory = save_learning(
    strategy
)

print(decision)
print(outcome)
print(feedback)
print(strategy)
print(memory)
