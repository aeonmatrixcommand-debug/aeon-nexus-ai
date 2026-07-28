from services.agent_economy.reputation.reputation_engine import ReputationEngine


def test_agent_reputation():

    engine = ReputationEngine()

    result = engine.evaluate("warehouse-agent")

    assert result["status"] == "trusted"
