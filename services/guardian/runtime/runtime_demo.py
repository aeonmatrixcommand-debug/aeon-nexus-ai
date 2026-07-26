from services.guardian.integration.ai_gateway_adapter import (
    AIGatewayAdapter
)

from services.guardian.integration.telemetry_adapter import (
    publish_decision
)


gateway=AIGatewayAdapter()


response=gateway.request(
    "DemandForecast",
    {
        "inventory":100,
        "demand":150
    }
)


publish_decision(
    "DemandForecast",
<<<<<<< HEAD
    response["decision"],
    response["confidence"],
=======
    response.decision,
    response.confidence,
>>>>>>> origin/main
    "LOW"
)


print(response)
