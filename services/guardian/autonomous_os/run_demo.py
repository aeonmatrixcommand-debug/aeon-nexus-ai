from services.guardian.autonomous_os.autonomous_os import AutonomousOperatingSystem


system = AutonomousOperatingSystem()

print(
    system.process(
        {
            "module": "DemandForecast",
            "risk": "HIGH",
            "confidence": 0.95
        }
    )
)
