from services.aeon_platform.runtime_gateway import RuntimeGateway


def test_gateway_health():
    gateway = RuntimeGateway()

    result = gateway.health()

    assert result["platform"] == "AEON MATRIX"
    assert result["status"] == "ONLINE"


def test_owner_dashboard():
    gateway = RuntimeGateway()

    result = gateway.owner_dashboard()

    assert result["digital_twin"] == "ACTIVE"
