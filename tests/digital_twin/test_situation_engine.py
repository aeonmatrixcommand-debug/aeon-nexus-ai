from digital_twin.dashboard.situation_engine import SituationEngine


class MockTwin:

    risks = [
        {
            "type": "cold_chain_breach"
        }
    ]


def test_situation_analysis():

    engine = SituationEngine()

    result = engine.analyze(MockTwin())

    assert result["status"] == "attention_required"
    assert result["priority"] == "high"
