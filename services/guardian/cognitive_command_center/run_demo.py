from .dashboard.executive_dashboard import generate
from .signal.signal_aggregator import aggregate
from .kpi.kpi_engine import analyze
from .decision.decision_feed import generate as decision
from .memory.command_memory import save


dashboard = generate(
    "ALL_SYSTEMS_OPERATIONAL"
)

signals = aggregate(
    [
        "INVENTORY_SIGNAL",
        "MARKET_SIGNAL",
        "RISK_SIGNAL"
    ]
)

kpi = analyze(
    [
        "OTIF",
        "COST",
        "PRODUCTIVITY"
    ]
)

recommendation = decision(
    kpi
)

print(dashboard)
print(signals)
print(kpi)
print(recommendation)
print(save(recommendation))
