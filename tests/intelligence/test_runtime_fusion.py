from src.intelligence.mother_brain.runtime import (
    MotherBrainRuntime,
)


def test_autonomous_runtime_flow():

    runtime = MotherBrainRuntime()

    result = runtime.process(
        "inventory risk detected"
    )

    assert result.signal
    assert result.action
    assert result.confidence >= 0
