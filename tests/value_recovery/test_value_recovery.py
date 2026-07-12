from services.guardian.value_recovery.runtime import ValueRecoveryIntelligence


def test_value_recovery():
    assert ValueRecoveryIntelligence().recover(
        {"recoverable_value": 500}
    )["action"] == "recover"

    assert ValueRecoveryIntelligence().recover(
        {"recoverable_value": 0}
    )["action"] == "discard"
