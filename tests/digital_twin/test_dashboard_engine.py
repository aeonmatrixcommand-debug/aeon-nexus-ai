from digital_twin.dashboard.dashboard_engine import DashboardEngine


class MockTwin:

    risks = [
        {
            "type": "cold_chain_breach",
            "severity": "high",
            "reason": "temperature abnormal"
        }
    ]

    impacts = {
        "financial_loss": 85000
    }


def test_dashboard_generation():

    engine = DashboardEngine()

    result = engine.generate(MockTwin())

    assert result["situation"] == "attention_required"
    assert len(result["risk_summary"]) == 1
    assert result["impact_summary"]["financial_loss"] == 85000
