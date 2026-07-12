from services.digital_twin.offline_engine import OfflineDigitalTwinEngine

def test_import():
    assert OfflineDigitalTwinEngine().status()["mode"] == "offline_predictive"
