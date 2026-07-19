from .collector.global_signal import collect
from .analyzer.future_analyzer import analyze
from .impact.impact_engine import evaluate
from .preparedness.action_engine import recommend
from .memory.future_memory import save


signal = collect(
    "GLOBAL_TECHNOLOGY_ECONOMIC_SIGNAL"
)

analysis = analyze(
    signal
)

impact = evaluate(
    analysis
)

action = recommend(
    impact
)

print(signal)
print(analysis)
print(impact)
print(action)
print(save(action))
