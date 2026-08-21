import pytest

from src.intelligence.ecdt.scenario_engine import ECDTScenarioEngine


def observed():
    return {
        "capacity": 0.95,
        "demand": 1.10,
        "inventory_risk": 0.30,
    }


def scenarios():
    return [
        {
            "name": "baseline",
            "impact_score": 0.40,
            "risk_score": 0.10,
            "confidence": 0.90,
        },
        {
            "name": "dynamic_labor_scaling",
            "impact_score": 0.80,
            "risk_score": 0.20,
            "confidence": 0.95,
        },
    ]


def test_scenario_engine_is_deterministic():
    engine = ECDTScenarioEngine()

    first = engine.evaluate(
        observed_state=observed(),
        scenarios=scenarios(),
    )
    second = engine.evaluate(
        observed_state=observed(),
        scenarios=scenarios(),
    )

    assert first == second


def test_best_scenario_is_recommended():
    result = ECDTScenarioEngine().evaluate(
        observed_state=observed(),
        scenarios=scenarios(),
    )

    assert result["status"] == "EVALUATED"
    assert result["executed"] is False
    assert result["recommended"]["name"] == "dynamic_labor_scaling"
    assert result["recommended"]["rank"] == 1


def test_policy_can_block_all_scenarios():
    result = ECDTScenarioEngine().evaluate(
        observed_state=observed(),
        scenarios=scenarios(),
        policy={"allowed": False},
    )

    assert result["recommended"] is None
    assert all(
        item["status"] == "POLICY_BLOCKED"
        for item in result["results"]
    )


def test_trace_is_present_for_audit():
    result = ECDTScenarioEngine().evaluate(
        observed_state=observed(),
        scenarios=scenarios(),
    )

    assert result["results"][0]["trace"]
    assert result["governance"]["execution_authorized"] is False


def test_missing_observed_state_raises():
    with pytest.raises(ValueError):
        ECDTScenarioEngine().evaluate(
            observed_state=None,
            scenarios=scenarios(),
        )


def test_missing_scenarios_raises():
    with pytest.raises(ValueError):
        ECDTScenarioEngine().evaluate(
            observed_state=observed(),
            scenarios=[],
        )


def test_invalid_metric_raises():
    data = scenarios()
    data[0]["risk_score"] = "not-a-number"

    with pytest.raises(ValueError):
        ECDTScenarioEngine().evaluate(
            observed_state=observed(),
            scenarios=data,
        )


def test_engine_has_no_execution_interface():
    engine = ECDTScenarioEngine()

    for name in (
        "execute",
        "executor",
        "apply",
        "deploy",
        "promote",
    ):
        assert not hasattr(engine, name)
