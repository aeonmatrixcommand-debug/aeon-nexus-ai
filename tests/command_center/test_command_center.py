from services.guardian.command_center.runtime import CommandCenter


def test_command_center():
    result = CommandCenter().status(
        {"otif": 99}
    )

    assert result["system"] == "AEONMATRIX"
    assert result["health"] == "green"
