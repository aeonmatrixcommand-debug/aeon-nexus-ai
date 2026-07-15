from digital_twin.impact.impact_engine import ImpactEngine


def test_impact():

    result = ImpactEngine().analyze(
        "reroute_vehicle"
    )

    assert result["sla_impact"] == "improved"
