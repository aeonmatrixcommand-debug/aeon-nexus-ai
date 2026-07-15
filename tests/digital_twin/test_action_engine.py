from digital_twin.governance.action_engine import ActionEngine


def test_action():

    result = ActionEngine().execute(
        "optimize_route"
    )

    assert result["status"] == "executed"
