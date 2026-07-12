from services.guardian.digital_twin.runtime import DigitalTwinRuntime

def test_simulation():
    twin = DigitalTwinRuntime()
    result = twin.simulate({"name": "peak_demand"})
    assert result["status"] == "completed"
    assert "risk_score" in result
