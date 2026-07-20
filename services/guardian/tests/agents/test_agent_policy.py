from services.guardian.agents.economy.policy import validate_agent_action


def test_policy():

    assert validate_agent_action(0.95)
