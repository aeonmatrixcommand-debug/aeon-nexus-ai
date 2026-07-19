from .context.context_engine import understand
from .reasoning.impact_reasoning import analyze
from .insight.executive_insight import generate
from .decision.decision_layer import decide
from .memory.cognitive_memory import save


context = understand(
    "SUPPLY_CHAIN_RISK_EVENT"
)

impact = analyze(
    context
)

insight = generate(
    impact
)

decision = decide(
    insight
)

print(context)
print(impact)
print(insight)
print(decision)
print(save(decision))
