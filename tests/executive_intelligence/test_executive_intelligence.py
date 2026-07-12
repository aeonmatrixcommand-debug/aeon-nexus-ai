from services.guardian.executive_intelligence.runtime import ExecutiveIntelligence

def test_executive():
    assert ExecutiveIntelligence().analyze({"kpi":"OTIF"})["decision"] == "recommend"
