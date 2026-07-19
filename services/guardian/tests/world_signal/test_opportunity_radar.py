from services.guardian.world_signal_intelligence.signal_collector import WorldSignalCollector
from services.guardian.world_signal_intelligence.intelligence_engine import SignalIntelligenceEngine
from services.guardian.world_signal_intelligence.opportunity_radar import OpportunityRadar
from services.guardian.strategy.executive_strategy import ExecutiveStrategyEngine


def test_world_signal_opportunity_flow():

    signal = WorldSignalCollector().collect({
        "market_signal": "GROWTH",
        "supply_signal": "RISK",
        "demand_signal": "HIGH"
    })

    intelligence = SignalIntelligenceEngine().analysis(signal)

    opportunity = OpportunityRadar().detect(
        intelligence
    )

    strategy = ExecutiveStrategyEngine().recommend(
        opportunity
    )

    assert intelligence["status"] == "OPPORTUNITY"
    assert opportunity["opportunity"]
    assert strategy["strategic_action"] == "EXPAND_CAPACITY"
