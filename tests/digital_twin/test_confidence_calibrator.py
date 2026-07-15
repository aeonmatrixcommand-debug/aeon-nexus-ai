from digital_twin.learning.confidence_calibrator import ConfidenceCalibrator


def test_calibration():

    result = ConfidenceCalibrator().calibrate(
        0.91,
        0.95
    )

    assert result["status"] == "calibrated"
