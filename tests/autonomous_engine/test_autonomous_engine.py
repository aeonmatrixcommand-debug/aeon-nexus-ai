from services.guardian.autonomous_engine.runtime import AutonomousEngine


def test_autonomous_engine_escalate():
    result = AutonomousEngine().decide(
        {"risk_score": 0.9}
    )

    assert result["action"] == "escalate"
    assert result["governance"] == "approved"


def test_autonomous_engine_monitor():
    result = AutonomousEngine().decide(
        {"risk_score": 0.6}
    )

    assert result["action"] == "monitor"


def test_autonomous_engine_execute():
    result = AutonomousEngine().decide(
        {"risk_score": 0.2}
    )

    assert result["action"] == "execute"
