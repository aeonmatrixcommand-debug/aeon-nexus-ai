from digital_twin.runtime.decision_runtime import DecisionRuntime


class MockTwin:

    def __init__(self):

        self.risks = [
            {
                "type": "cold_chain_breach"
            }
        ]


def test_decision_runtime():

    twin = MockTwin()

    result = DecisionRuntime().execute(
        twin
    )

    assert (
        result.decision_result["recommendation"]
        ["action"]
        == "move_to_backup_storage"
    )

    assert (
        result.decision_result["confidence"]
        ["confidence"]
        > 0.9
    )
