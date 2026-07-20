from .tracker.outcome_tracker import OutcomeTracker
from .reflection.reflection_engine import ReflectionEngine
from .scoring.decision_score import calculate_score
from .learning.learning_signal import create_learning_signal


outcome = OutcomeTracker().record(
    "INVENTORY_OPTIMIZATION",
    "SUCCESS"
)

reflection = ReflectionEngine().analyze(
    outcome
)

score = calculate_score(
    outcome
)

signal = create_learning_signal(
    score
)

print(outcome)
print(reflection)
print(signal)
