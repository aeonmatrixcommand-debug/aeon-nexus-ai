from services.digital_twin.gps import GpsEngine
from services.digital_twin.eta import EtaEngine
from services.digital_twin.route import RouteEngine
from services.digital_twin.risk import RiskEngine

def test_health():
    assert GpsEngine().health()["status"]=="healthy"
    assert EtaEngine().health()["status"]=="healthy"
    assert RouteEngine().health()["status"]=="healthy"
    assert RiskEngine().health()["status"]=="healthy"
