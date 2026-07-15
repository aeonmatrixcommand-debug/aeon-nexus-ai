from digital_twin.governance.approval_engine import ApprovalEngine


def test_approval():

    result = ApprovalEngine().request(
        "shutdown_operation"
    )

    assert result["human_required"] is True
