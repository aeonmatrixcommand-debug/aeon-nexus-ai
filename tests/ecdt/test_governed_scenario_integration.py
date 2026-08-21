from src.intelligence.ecdt import (
    ECDTExecutionMode,
    ECDTGovernedScenarioIntegration,
    ECDTRuntime,
)


def signals():
    return [
        {
            "source": "WMS",
            "metric": "capacity",
            "value": 0.95,
        }
    ]


def risk():
    return {
        "type": "capacity_shortage",
    }


def observed_state():
    return {
        "capacity": 0.95,
        "demand": 1.10,
    }


def candidates(action="optimize_capacity"):
    return [
        {
            "name": "baseline",
            "impact_score": 0.30,
            "risk_score": 0.10,
            "confidence": 0.90,
            "action": "optimize_capacity",
        },
        {
            "name": "dynamic_labor_scaling",
            "impact_score": 0.90,
            "risk_score": 0.10,
            "confidence": 0.95,
            "action": action,
            "runtime_scenario": {
                "name": "dynamic_labor_scaling",
            },
        },
    ]


def test_recommendation_routes_to_runtime_dry_run():
    integration = ECDTGovernedScenarioIntegration()

    result = integration.run(
        signals=signals(),
        risk=risk(),
        observed_state=observed_state(),
        scenarios=candidates(),
    )

    assert result["scenario_evaluation"]["recommended"]["name"] == (
        "dynamic_labor_scaling"
    )
    assert result["recommendation_is_authority"] is False
    assert result["status"] == "DRY_RUN"
    assert result["executed"] is False
    assert result["runtime"]["executed"] is False


def test_policy_blocked_scenarios_never_reach_runtime():
    integration = ECDTGovernedScenarioIntegration()

    result = integration.run(
        signals=signals(),
        risk=risk(),
        observed_state=observed_state(),
        scenarios=candidates(),
        policy={"allowed": False},
    )

    assert result["status"] == "NO_RECOMMENDATION"
    assert result["executed"] is False
    assert "runtime" not in result


def test_restricted_action_still_requires_human():
    integration = ECDTGovernedScenarioIntegration()

    result = integration.run(
        signals=signals(),
        risk=risk(),
        observed_state=observed_state(),
        scenarios=candidates(action="delete_inventory"),
    )

    assert result["status"] == "HUMAN_REQUIRED"
    assert result["executed"] is False
    assert result["runtime"]["governance"]["approval"]["human_required"] is True


def test_guard_block_cannot_be_bypassed_by_recommendation():
    integration = ECDTGovernedScenarioIntegration()

    result = integration.run(
        signals=signals(),
        risk=risk(),
        observed_state=observed_state(),
        scenarios=candidates(action="shutdown_system"),
        human_approved=True,
    )

    assert result["status"] == "BLOCKED"
    assert result["executed"] is False


def test_execute_mode_still_requires_executor():
    runtime = ECDTRuntime(
        execution_mode=ECDTExecutionMode.EXECUTE,
    )

    integration = ECDTGovernedScenarioIntegration(
        runtime=runtime,
    )

    result = integration.run(
        signals=signals(),
        risk=risk(),
        observed_state=observed_state(),
        scenarios=candidates(),
    )

    assert result["status"] == "EXECUTOR_REQUIRED"
    assert result["executed"] is False


def test_missing_action_does_not_execute():
    data = candidates()
    data[1].pop("action")

    integration = ECDTGovernedScenarioIntegration()

    result = integration.run(
        signals=signals(),
        risk=risk(),
        observed_state=observed_state(),
        scenarios=data,
    )

    assert result["status"] == "ACTION_REQUIRED"
    assert result["executed"] is False
    assert "runtime" not in result


def test_integration_has_no_direct_execution_interface():
    integration = ECDTGovernedScenarioIntegration()

    for name in (
        "execute",
        "apply",
        "deploy",
        "promote",
    ):
        assert not hasattr(integration, name)
