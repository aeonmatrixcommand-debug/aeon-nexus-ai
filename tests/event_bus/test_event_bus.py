from services.guardian.event_bus.runtime import EventBus

def test_event_bus():
    assert EventBus().publish({"type":"ORDER"})["event_status"] == "published"
