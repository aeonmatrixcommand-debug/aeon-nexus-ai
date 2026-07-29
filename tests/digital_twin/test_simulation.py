from services.digital_twin.simulation.scenario_engine import ScenarioEngine


def test_simulation():

    engine = ScenarioEngine()

    result = engine.simulate("inventory shortage")

    assert result["result"] == "simulated"
