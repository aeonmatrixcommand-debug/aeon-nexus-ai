from digital_twin.adaptive.pattern_engine import PatternEngine


def test_pattern_detection():

    result = PatternEngine().detect(
        [
            "cold_chain_breach",
            "temperature_alert"
        ]
    )

    assert result["pattern_count"] == 1
