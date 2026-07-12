from services.guardian.demand_forecast.runtime import DemandForecastEngine


def test_forecast():
    result = DemandForecastEngine().forecast(
        {"demand": 150}
    )

    assert result["trend"] == "growth"

    result = DemandForecastEngine().forecast(
        {"demand": 50}
    )

    assert result["trend"] == "stable"
