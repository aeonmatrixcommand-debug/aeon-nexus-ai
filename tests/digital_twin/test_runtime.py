from services.digital_twin.runtime import DigitalTwinRuntime

def test_runtime():
    status = DigitalTwinRuntime().status()
    assert status["runtime"] == "healthy"
    assert status["offline"]["mode"] == "offline_predictive"
