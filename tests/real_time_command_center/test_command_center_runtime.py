from services.guardian.real_time_command_center.runtime import RealTimeCommandCenter


def test_command_center_monitor():
    result = RealTimeCommandCenter().monitor(
        {"severity": "critical", "source": "warehouse"}
    )

    assert result["status"] == "alert"

    result = RealTimeCommandCenter().monitor(
        {"severity": "normal"}
    )

    assert result["status"] == "monitoring"
