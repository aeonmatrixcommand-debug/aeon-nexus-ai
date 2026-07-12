from services.guardian.risk_engine.runtime import RiskEngine


def test_risk_engine():
    assert RiskEngine().predict(
        {"risk_signal": 0.9}
    )["status"] == "high"

    assert RiskEngine().predict(
        {"risk_signal": 0.1}
    )["status"] == "normal"
