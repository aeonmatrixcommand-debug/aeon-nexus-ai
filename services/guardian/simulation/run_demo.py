from services.guardian.simulation.digital_twin_loop import DigitalTwinLoop

twin = DigitalTwinLoop()

print({
    "digital_twin_status": "ACTIVE",
    "result": twin.simulate(
        {
            "inventory": 100,
            "demand": 150
        }
    )
})
