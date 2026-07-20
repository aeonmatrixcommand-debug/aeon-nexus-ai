from services.guardian.digital_twin_live.twin_engine import update_twin
from services.guardian.simulation.what_if import run_scenario


def test_multiple_scenario():

    twin = update_twin({
        "warehouse": "DC01",
        "inventory": 200,
        "demand": 100,
        "risk": 0.2
    })

    result = run_scenario(
        twin,
        [-20, 0, 50]
    )

    assert len(result) == 3
