from services.guardian.control_tower.signal import RuntimeSignal
from services.guardian.control_tower.decision_center import analyze_signal
from services.guardian.control_tower.action_router import route_action


def test_high_risk_signal():

    signal = RuntimeSignal(
        "RiskEngine",
        "RISK",
        "HIGH",
        0.95
    )

    decision = analyze_signal(signal)

    action = route_action(decision)

    assert action["status"] == "READY"
