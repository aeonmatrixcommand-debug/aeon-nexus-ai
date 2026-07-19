from services.guardian.agents.economy.marketplace import publish_task
from services.guardian.agents.economy.negotiator import negotiate


def test_marketplace():

    result = publish_task({
        "name": "Demand Forecast",
        "skill": "Demand Intelligence"
    })

    assert "Forecast Agent" in result["candidates"]


def test_negotiation():

    result = negotiate(
        "Demand Intelligence"
    )

    assert result["confidence"] >= 0.9
