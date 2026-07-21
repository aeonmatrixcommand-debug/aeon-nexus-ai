<<<<<<< HEAD
from .collector.signal_collector import collect
from .analysis.trend_analyzer import analyze
from .risk.future_risk_detector import detect
from .opportunity.opportunity_engine import identify
from .memory.signal_memory import save
=======
from services.guardian.world_signal_intelligence.collector.signal_collector import collect
from services.guardian.world_signal_intelligence.analysis.trend_analyzer import analyze
from services.guardian.world_signal_intelligence.risk.future_risk_detector import detect
from services.guardian.world_signal_intelligence.opportunity.opportunity_engine import identify
from services.guardian.world_signal_intelligence.memory.signal_memory import save
>>>>>>> 1df4713 (fix: migrate guardian imports to services namespace)


signal = collect(
    "GLOBAL_MARKET",
    "AI_SUPPLY_CHAIN_TRANSFORMATION"
)

trend = analyze(
    signal
)

risk = detect(
    trend
)

opportunity = identify(
    signal
)

print(signal)
print(trend)
print(risk)
print(opportunity)
print(save(opportunity))
