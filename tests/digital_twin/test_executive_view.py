from digital_twin.dashboard.executive_view import ExecutiveView


def test_executive_view():

    engine = ExecutiveView()

    situation = {
        "status": "attention_required",
        "title": "Operational Risk Detected"
    }

    insight = {
        "impact": ["Operational disruption"]
    }

    result = engine.generate(
        situation,
        insight,
        {"financial_loss": 85000}
    )

    assert result["confidence"] > 0
    assert result["business_impact"]["financial_loss"] == 85000
    assert len(result["decision_required"]) > 0
