from src.intelligence.risk.predictor import RiskPredictor
from src.intelligence.eta.predictor import ETAPredictor
from src.intelligence.demand.shock_detector import DemandShockDetector


def test_risk_prediction():

    result = RiskPredictor().predict(
        ["delay", "capacity"]
    )

    assert result["risk_score"] == 0.2


def test_eta_prediction():

    result = ETAPredictor().predict(
        100,
        50,
    )

    assert result["eta_hours"] == 2


def test_demand_shock():

    result = DemandShockDetector().detect(
        100,
        130,
    )

    assert result["shock_detected"]
