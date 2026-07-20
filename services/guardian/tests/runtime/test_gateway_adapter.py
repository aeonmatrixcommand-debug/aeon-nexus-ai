from services.guardian.integration.ai_gateway_adapter import (
AIGatewayAdapter
)


def test_gateway():

    r=AIGatewayAdapter().request(
        "DemandForecast",
        {}
    )

    assert r["policy"]=="APPROVED"
