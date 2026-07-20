from .collector.signal_collector import collect
from .analysis.trend_analyzer import analyze
from .risk.future_risk_detector import detect
from .opportunity.opportunity_engine import identify
from .memory.signal_memory import save


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
