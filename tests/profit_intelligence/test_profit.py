from services.guardian.profit_intelligence.runtime import ProfitIntelligence

def test_profit():
    assert ProfitIntelligence().predict({})["profit_impact"] == "positive"
