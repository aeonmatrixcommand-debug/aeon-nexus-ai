from services.agent.reward.evaluator import RewardEvaluator


def test_reward_evaluation():

    evaluator = RewardEvaluator()

    reward = evaluator.evaluate(
        agent_id="AEON-001",
        task="inventory_prediction",
        success=True
    )

    assert reward.agent_id == "AEON-001"
    assert reward.score == 1.0
