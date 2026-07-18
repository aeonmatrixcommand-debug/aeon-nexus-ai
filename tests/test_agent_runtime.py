from ai.orchestration.planner import plan


def test_inventory_agent():
    result = plan(
        "inventory_check",
        location="DC01"
    )

    assert result["status"] == "ready"


def test_risk_agent():
    result = plan(
        "risk_analysis",
        area="Warehouse-A"
    )

    assert "risk_score" in result
