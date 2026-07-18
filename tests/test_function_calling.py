from ai.function_calling.router import execute_tool


def test_inventory_tool():
    result = execute_tool(
        "get_inventory",
        location="DC01"
    )

    assert result["status"] == "ready"


def test_risk_tool():
    result = execute_tool(
        "analyze_risk",
        area="Warehouse-A"
    )

    assert "risk_score" in result
