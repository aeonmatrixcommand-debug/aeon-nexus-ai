from services.guardian.learning.intelligence.learning_memory import memory
from services.guardian.learning.intelligence.pattern_detector import detect_pattern
from services.guardian.learning.intelligence.optimization_engine import optimize


def publish_learning(event):
    memory.store(event)

    pattern = detect_pattern(memory.history())

    return optimize(pattern)
