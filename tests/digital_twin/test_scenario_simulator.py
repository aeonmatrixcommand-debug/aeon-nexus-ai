from digital_twin.simulation.scenario_simulator import ScenarioSimulator


def test_scenario():

    result = ScenarioSimulator().simulate(
        "volume_increase"
    )

    assert result["status"] == "simulated"
