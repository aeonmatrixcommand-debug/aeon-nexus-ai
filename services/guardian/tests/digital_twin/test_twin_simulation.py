from services.guardian.digital_twin_live.twin_engine import update_twin
from services.guardian.simulation.scenario_engine import simulate
from services.guardian.simulation.predictive_engine import predict


def test_prediction_flow():

    twin = update_twin({
        "warehouse": "DC01",
        "inventory": 100,
        "demand": 150,
        "risk": 0.5
    })

    result = simulate(
        twin,
        50
    )

    prediction = predict(result)

    assert "prediction" in prediction
    assert prediction["confidence"] >= 0
