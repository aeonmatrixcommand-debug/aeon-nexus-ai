from services.guardian.execution.execution_layer import AutonomousExecutionLayer


def test_execution_layer():

    engine = AutonomousExecutionLayer()

    result = engine.run(
        {
            "action": "ALLOCATE_STOCK",
            "confidence": 0.94
        }
    )

    assert result["execution"]["status"] == "EXECUTED"
