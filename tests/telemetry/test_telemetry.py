from services.guardian.telemetry.runtime import Telemetry

def test_telemetry():
    assert Telemetry().collect({"cpu":10})["telemetry_status"] == "received"
