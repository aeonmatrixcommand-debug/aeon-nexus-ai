from services.guardian.digital_twin_simulation.runtime import DigitalTwinSimulation

def test_simulation():
    assert DigitalTwinSimulation().simulate("scenario")["simulation"] == "completed"
