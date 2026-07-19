from services.guardian.execution.execution_layer import AutonomousExecutionLayer


engine = AutonomousExecutionLayer()

print(
    engine.run(
        {
            "action": "INCREASE_ALLOCATION",
            "confidence": 0.94
        }
    )
)
