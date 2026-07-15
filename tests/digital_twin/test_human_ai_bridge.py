from digital_twin.cognition.human_ai_bridge import HumanAIBridge


def test_bridge():

    result = HumanAIBridge().translate(
        "temperature anomaly",
        "สินค้ามีความเสี่ยง",
        "reroute vehicle"
    )

    assert result["alignment"] == "complete"
