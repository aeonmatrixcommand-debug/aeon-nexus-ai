from digital_twin.sustainability.sustainability_engine import SustainabilityEngine


def test_sustainability():

    result = SustainabilityEngine().analyze(
        "transport_operation"
    )

    assert result["carbon"] == "optimized"
