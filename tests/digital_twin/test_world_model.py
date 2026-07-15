from digital_twin.prediction.trend_engine import TrendEngine
from digital_twin.prediction.scenario_forecaster import ScenarioForecaster
from digital_twin.world_model.world_state import WorldState


def test_trend_analysis():

    result = TrendEngine().analyze({
        "demand_growth":0.4,
        "capacity":0.9
    })

    assert result["trend"] == "growth"
    assert result["risk"] == "capacity_pressure"


def test_scenario_forecast():

    result = ScenarioForecaster().forecast(
        "increase_capacity"
    )

    assert result["otif"] == 0.97


def test_world_alignment():

    world = WorldState()

    world.human_view = {
        "problem":"warehouse capacity"
    }

    world.ai_view = {
        "prediction":"future bottleneck"
    }

    result = world.synchronize()

    assert result["aligned"] is True
