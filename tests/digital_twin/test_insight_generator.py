from digital_twin.dashboard.insight_generator import InsightGenerator


def test_generate_insight():

    engine = InsightGenerator()

    situation = {
        "status": "attention_required"
    }

    result = engine.generate(situation)

    assert len(result["impact"]) > 0
    assert len(result["indirect_effects"]) > 0
    assert len(result["opportunities"]) > 0
