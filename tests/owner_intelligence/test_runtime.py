from services.owner_intelligence.runtime import OwnerIntelligenceRuntime


def test_business_snapshot():
    runtime = OwnerIntelligenceRuntime()

    data = runtime.get_business_snapshot()

    assert data["revenue_intelligence"] == "ACTIVE"
    assert data["supply_chain_twin"] == "ACTIVE"


def test_executive_summary():
    runtime = OwnerIntelligenceRuntime()

    result = runtime.executive_summary()

    assert result["system"] == "AEON MATRIX"
    assert result["mode"] == "OWNER COMMAND CENTER"
