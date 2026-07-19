from services.guardian.control_tower.event_bridge import create_event
from services.guardian.control_tower.decision_center import analyze_signal
from services.guardian.control_tower.signal import RuntimeSignal


def test_executive_signal():

    signal = RuntimeSignal(
        "DemandForecast",
        "FORECAST",
        "LOW",
        0.8
    )

    decision = analyze_signal(signal)

    event = create_event(decision)

    assert event["topic"] == "guardian.control.decision"
