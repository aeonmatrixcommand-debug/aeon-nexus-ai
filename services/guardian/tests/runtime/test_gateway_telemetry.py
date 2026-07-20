from services.guardian.integration.ai_gateway_adapter import AIGatewayAdapter
from services.guardian.telemetry.runtime.publisher import RuntimeTelemetryPublisher


def test_gateway_to_telemetry_flow():

    gateway = AIGatewayAdapter()
    telemetry = RuntimeTelemetryPublisher()

    signal = gateway.request(
        "DemandForecast",
        {
            "inventory": 100,
            "demand": 150
        }
    )

    assert gateway.validate(signal)

    event = telemetry.publish(signal)

    assert event["topic"] == "guardian.decision"
    assert event["confidence"] == 0.94
