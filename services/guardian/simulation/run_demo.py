from services.guardian.simulation.digital_twin_loop import DigitalTwinLoop


twin = DigitalTwinLoop()

result = twin.simulate(
    {
        "inventory": 100,
        "demand": 150
    }
)

print({
    "digital_twin_status": "ACTIVE",
    "result": result
})
