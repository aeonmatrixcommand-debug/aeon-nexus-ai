from digital_twin.models.twin_state import DigitalTwinState
from digital_twin.engine.risk_engine import RiskEngine


def test_create_digital_twin_state():

    twin = DigitalTwinState(
        entity_id="DC001",
        entity_type="warehouse"
    )

    twin.current_state = {
        "temperature": 10,
        "worker_capacity": 40
    }

    engine = RiskEngine()

    result = engine.analyze(twin)

    assert len(result.risks) == 2

    assert result.risks[0]["type"] == "cold_chain_breach"
