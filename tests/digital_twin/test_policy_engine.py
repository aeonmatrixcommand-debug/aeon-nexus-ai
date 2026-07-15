from digital_twin.governance.policy_engine import PolicyEngine


def test_policy():

    result = PolicyEngine().check(
        "reroute_delivery"
    )

    assert result["allowed"] is True
