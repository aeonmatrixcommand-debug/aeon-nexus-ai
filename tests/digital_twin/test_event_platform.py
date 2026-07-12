from services.digital_twin.event_bus import EventBus
from services.digital_twin.telemetry import TelemetryEngine
from services.digital_twin.simulation import SimulationEngine

def test_platform():
    assert EventBus().health()["status"]=="healthy"
    assert TelemetryEngine().health()["status"]=="healthy"
    assert SimulationEngine().health()["status"]=="healthy"
