from digital_twin.cognition.shared_context import SharedContext


def test_shared_context():

    result = SharedContext().build(
        "cold_chain_risk",
        "temperature anomaly"
    )

    assert result["alignment"] == "shared"
