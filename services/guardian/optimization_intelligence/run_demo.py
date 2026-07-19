from .engine.optimization_engine import analyze
from .analysis.performance_analyzer import evaluate
from .recommendation.action_recommender import recommend
from .value.value_impact import calculate
from .feedback.learning_feedback import generate
from .memory.optimization_memory import save


operation = {
    "area": "WAREHOUSE_OPERATION",
    "target": "PRODUCTIVITY"
}


analysis = analyze(operation)

performance = evaluate(analysis)

recommendation = recommend(performance)

value = calculate(recommendation)

feedback = generate(value)

memory = save(
    {
        "analysis": analysis,
        "performance": performance,
        "recommendation": recommendation,
        "value": value,
        "feedback": feedback
    }
)


print(analysis)
print(performance)
print(recommendation)
print(value)
print(feedback)
print(memory)
