from services.guardian.simulation.digital_twin_loop import DigitalTwinLoop


def test_digital_twin_simulation():
    twin = DigitalTwinLoop()

    result = twin.simulate(
        {
            "inventory": 100,
            "demand": 150
        }
    )

    assert result["impact"]["risk"] == "HIGH"
