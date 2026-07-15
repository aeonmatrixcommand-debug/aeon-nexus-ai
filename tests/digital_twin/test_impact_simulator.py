from digital_twin.business.impact_simulator import ImpactSimulator


def test_business_impact():

    result = ImpactSimulator().simulate(
        "demand_increase"
    )

    assert result["roi"] == "calculated"
