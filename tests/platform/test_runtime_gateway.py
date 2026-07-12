from services.platform.runtime_gateway import RuntimeGateway


def test_runtime_gateway_health():
    gateway = RuntimeGateway()

    result = gateway.health()

    assert result["platform"] == "AEON MATRIX"
    assert "digital_twin" in result
