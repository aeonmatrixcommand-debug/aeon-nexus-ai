from src.intelligence.digital_twin.twin_state import (
    TwinStateManager,
)

from src.intelligence.digital_twin.confidence_index import (
    ConfidenceIndexEngine,
)

from src.intelligence.digital_twin.simulation_engine import (
    SimulationEngine,
)


def test_digital_twin_flow():

    twin = TwinStateManager()

    state = twin.create_state(
        "inventory",
        "SKU-001",
        "risk",
        {
            "quantity": 100,
        },
    )

    assert state.entity_type == "inventory"

    confidence = ConfidenceIndexEngine().calculate(
        0.9,
        0.95,
        0.85,
    )

    assert confidence > 0

    result = SimulationEngine().simulate(
        state.metrics,
        {
            "demand": "increase",
        },
    )

    assert result["impact"]
