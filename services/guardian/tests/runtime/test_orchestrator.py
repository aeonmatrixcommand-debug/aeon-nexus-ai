from services.guardian.runtime.orchestration.runtime_orchestrator import RuntimeOrchestrator


def test_runtime_orchestration():

    runtime = RuntimeOrchestrator()

    result = runtime.execute(
        "Demand Forecast Optimization"
    )

    assert result is not None
