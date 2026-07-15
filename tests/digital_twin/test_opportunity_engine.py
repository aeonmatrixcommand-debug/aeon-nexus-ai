from digital_twin.opportunity.opportunity_engine import OpportunityEngine
from digital_twin.opportunity.value_simulator import ValueSimulator


class Twin:
    signals = {
        "demand_growth": 0.35
    }


def test_opportunity_detection():

    result = OpportunityEngine().detect(Twin())

    assert len(result) > 0
    assert result[0]["type"] == "capacity_expansion"


def test_value_simulation():

    result = ValueSimulator().simulate({
        "type": "capacity_expansion"
    })

    assert result["confidence"] > 0
