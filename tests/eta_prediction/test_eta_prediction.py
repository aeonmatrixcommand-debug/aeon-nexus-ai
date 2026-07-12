from services.guardian.eta_prediction.runtime import ETAPredictionEngine


def test_eta():
    assert ETAPredictionEngine().predict(
        {"delay": 60}
    )["eta_status"] == "delayed"

    assert ETAPredictionEngine().predict(
        {"delay": 10}
    )["eta_status"] == "on_time"
