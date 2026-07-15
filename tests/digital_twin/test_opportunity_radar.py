from digital_twin.opportunity.opportunity_radar import OpportunityRadar


def test_opportunity():

    result = OpportunityRadar().detect(
        "demand_increase"
    )

    assert result["opportunity"] == "identified"
