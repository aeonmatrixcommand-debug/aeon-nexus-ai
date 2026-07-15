from digital_twin.world_signal.world_signal_runtime import WorldSignalRuntime


def test_world_runtime():

    result = WorldSignalRuntime().execute(
        [
            "fuel_price_increase"
        ]
    )

    assert len(result["insights"]["insights"]) == 1
    assert len(result["opportunities"]) == 1
