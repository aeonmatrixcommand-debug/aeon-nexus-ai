from services.agent.autonomy.autonomous_engine import AutonomousEngine


def test_agent_autonomy():

    agent = AutonomousEngine()

    result = agent.observe("inventory_change")

    assert result["status"] == "OBSERVED"


def test_agent_decision():

    agent = AutonomousEngine()

    decision = agent.decide({
        "risk": "LOW"
    })

    assert decision["decision"] == "OPTIMIZE"
