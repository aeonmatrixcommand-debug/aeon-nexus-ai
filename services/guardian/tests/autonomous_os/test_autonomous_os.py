from services.guardian.autonomous_os.autonomous_os import AutonomousOperatingSystem


def test_autonomous_os():

    system = AutonomousOperatingSystem()

    result = system.process(
        {
            "risk": "HIGH",
            "confidence": 0.95
        }
    )

    assert result["recovery"]["status"] == "TRIGGERED"
    assert result["learning"]["learning_allowed"] is True
