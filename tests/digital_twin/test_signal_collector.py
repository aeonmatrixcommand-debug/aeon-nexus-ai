from digital_twin.world_signal.signal_collector import SignalCollector


def test_signal_collection():

    result = SignalCollector().collect(
        [
            "weather_disruption"
        ]
    )

    assert result["signal_count"] == 1
