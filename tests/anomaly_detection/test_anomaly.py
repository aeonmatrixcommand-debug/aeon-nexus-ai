from services.guardian.anomaly_detection.runtime import AnomalyDetection

def test_anomaly():
    assert AnomalyDetection().analyze(100)["anomaly"]
