from digital_twin.decision.simulation_engine import SimulationEngine


def test_simulation():

    decision = {
        "action": "move_to_backup_storage"
    }

    result = SimulationEngine().simulate(decision)

    assert result["risk_reduction"] == 0.85
    assert result["sla_protection"] == "high"
