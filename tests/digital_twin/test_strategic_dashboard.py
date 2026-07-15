from digital_twin.executive.strategic_dashboard import StrategicDashboard


def test_dashboard():

    result = StrategicDashboard().generate()

    assert result["status"] == "ready"
