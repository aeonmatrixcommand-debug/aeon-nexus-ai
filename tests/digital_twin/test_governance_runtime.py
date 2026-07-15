from digital_twin.governance.governance_runtime import GovernanceRuntime


def test_governance_runtime():

    result = GovernanceRuntime().execute(
        "reroute_delivery"
    )

    assert (
        result["result"]["status"]
        ==
        "executed"
    )
