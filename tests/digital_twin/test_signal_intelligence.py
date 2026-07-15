from digital_twin.world_signal.signal_intelligence import SignalIntelligence


def test_signal_analysis():

    result = SignalIntelligence(). analyze(
        {
            "signals":[
                "fuel_price_increase"
            ]
        }
    )

    assert result["count"] == 1
