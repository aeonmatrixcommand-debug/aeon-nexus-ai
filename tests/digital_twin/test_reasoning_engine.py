from digital_twin.engine.reasoning_engine import ReasoningEngine


def test_reasoning():

    engine = ReasoningEngine()

    result = engine.explain(
        {
            "type":"cold_chain_breach"
        }
    )

    assert result["confidence"] > 0
    assert result["recommended_action"]
