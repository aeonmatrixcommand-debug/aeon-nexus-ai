from services.guardian.digital_twin_runtime.twin_state import TwinState
from services.guardian.digital_twin_runtime.simulator import TwinSimulator
from services.guardian.prediction.impact_engine import ImpactPredictionEngine
from services.guardian.prediction.recommendation_engine import RecommendationEngine


def test_digital_twin_prediction():

    state = TwinState().snapshot({
        "inventory": 100,
        "demand": 150,
        "risk": "HIGH"
    })

    simulation = TwinSimulator().simulate(state)

    prediction = ImpactPredictionEngine().predict(simulation)

    action = RecommendationEngine().recommend(prediction)

    assert prediction["impact_score"] == 0.9
    assert action == "INCREASE_ALLOCATION"
