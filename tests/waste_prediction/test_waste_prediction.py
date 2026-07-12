from services.guardian.waste_prediction.runtime import WastePredictionEngine


def test_waste_prediction():
    assert WastePredictionEngine().predict(
        {"expiry_risk": 0.9}
    )["status"] == "high"

    assert WastePredictionEngine().predict(
        {"expiry_risk": 0.2}
    )["status"] == "low"
