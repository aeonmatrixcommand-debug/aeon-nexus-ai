from digital_twin.prediction.risk_predictor import RiskPredictor


def test_risk_prediction():

    result = RiskPredictor().predict(
        ["temperature_high", "traffic_delay"]
    )

    assert result["priority"] == "high"
