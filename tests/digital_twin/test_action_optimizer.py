from digital_twin.prediction.action_optimizer import ActionOptimizer


def test_action_optimizer():

    result = ActionOptimizer().optimize(
        "cold_chain_failure"
    )

    assert result["recommended_action"] == "reroute"
