from digital_twin.governance.decision_trace import DecisionTrace


def test_decision_trace():

    result = DecisionTrace().generate(
        "cold_chain_breach",
        "cooling_failure",
        "85000_loss",
        "reroute_vehicle",
        0.91
    )

    assert result["trace_status"] == "complete"
