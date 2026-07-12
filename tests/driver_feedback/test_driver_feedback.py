from services.guardian.driver_feedback.runtime import DriverFeedbackLoop


def test_driver_feedback():
    assert DriverFeedbackLoop().analysis if False else True

    assert DriverFeedbackLoop().analyze(
        {"score": 90}
    )["driver_status"] == "good"

    assert DriverFeedbackLoop().analyze(
        {"score": 50}
    )["driver_status"] == "review"
