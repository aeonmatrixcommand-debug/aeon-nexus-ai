from .signal.customer_signal import analyze
from .trend.market_trend import detect
from .behavior.consumer_behavior import evaluate
from .opportunity.opportunity_engine import discover
from .memory.customer_memory import save


signal = analyze(
    "CUSTOMER_PURCHASE_PATTERN"
)

trend = detect(
    "RETAIL_MARKET"
)

behavior = evaluate(
    "CONSUMER_BEHAVIOR_SIGNAL"
)

opportunity = discover(
    signal
)

print(signal)
print(trend)
print(behavior)
print(opportunity)
print(save(opportunity))
