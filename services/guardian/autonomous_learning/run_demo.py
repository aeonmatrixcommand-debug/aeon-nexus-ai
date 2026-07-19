from .feedback.feedback_engine import collect
from .analysis.outcome_analyzer import analyze
from .optimization.optimizer import optimize
from .pattern.pattern_detector import detect
from .memory.learning_memory import save


feedback = collect(
    {
        "operation": "ORDER_FULFILLMENT",
        "result": "SUCCESS"
    }
)


analysis = analyze(
    feedback
)


optimization = optimize(
    analysis
)


pattern = detect(
    optimization
)


memory = save(
    pattern
)


print(feedback)
print(analysis)
print(optimization)
print(pattern)
print(memory)
