from digital_twin.decision.decision_engine import DecisionEngine


class MockTwin:
    def __init__(self):
        self.risks = [
            {
                "type": "cold_chain_breach"
            }
        ]


def test_decision_generation():

    twin = MockTwin()

    result = DecisionEngine().evaluate(twin)

    assert len(result.decisions) == 1
    assert result.decisions[0]["action"] == "move_to_backup_storage"
