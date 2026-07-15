from digital_twin.value.recovery_engine import ValueRecoveryEngine


def test_recovery():

    result = ValueRecoveryEngine().analyze(
        "inventory_waste"
    )

    assert result["recovery"] == "identified"
