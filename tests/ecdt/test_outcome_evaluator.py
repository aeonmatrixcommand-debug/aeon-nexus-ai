from src.intelligence.ecdt.outcome_evaluator import OutcomeEvaluator


def test_evaluates_numeric_outcome_variance():
    evaluator = OutcomeEvaluator()

    result = evaluator.evaluate(
        expected={
            "throughput": 100.0,
            "cost": 50.0,
        },
        observed={
            "throughput": 110.0,
            "cost": 45.0,
        },
    )

    assert result["evaluation"] is True
    assert result["executable"] is False
    assert result["metric_count"] == 2

    assert result["metrics"]["throughput"]["variance"] == 10.0
    assert (
        result["metrics"]["throughput"]["variance_percent"]
        == 10.0
    )

    assert result["metrics"]["cost"]["variance"] == -5.0
    assert (
        result["metrics"]["cost"]["absolute_variance"]
        == 5.0
    )


def test_only_shared_numeric_metrics_are_evaluated():
    evaluator = OutcomeEvaluator()

    result = evaluator.evaluate(
        expected={
            "throughput": 100,
            "scenario": "baseline",
            "expected_only": 12,
        },
        observed={
            "throughput": 90,
            "scenario": "actual",
            "observed_only": 15,
        },
    )

    assert result["metric_count"] == 1
    assert set(result["metrics"]) == {"throughput"}


def test_zero_expected_value_has_no_percentage_variance():
    evaluator = OutcomeEvaluator()

    result = evaluator.evaluate(
        expected={"failures": 0},
        observed={"failures": 2},
    )

    metric = result["metrics"]["failures"]

    assert metric["variance"] == 2
    assert metric["variance_percent"] is None


def test_boolean_values_are_not_numeric_metrics():
    evaluator = OutcomeEvaluator()

    result = evaluator.evaluate(
        expected={"healthy": True},
        observed={"healthy": False},
    )

    assert result["metric_count"] == 0
    assert result["metrics"] == {}


def test_inputs_are_not_mutated():
    evaluator = OutcomeEvaluator()

    expected = {
        "throughput": 100,
        "nested": {"source": "simulation"},
    }
    observed = {
        "throughput": 105,
        "nested": {"source": "telemetry"},
    }

    result = evaluator.evaluate(
        expected=expected,
        observed=observed,
    )

    result["expected"]["nested"]["source"] = "MUTATED"
    result["observed"]["nested"]["source"] = "MUTATED"

    assert expected["nested"]["source"] == "simulation"
    assert observed["nested"]["source"] == "telemetry"


def test_result_contains_independent_input_snapshots():
    evaluator = OutcomeEvaluator()

    expected = {"throughput": 100}
    observed = {"throughput": 110}

    result = evaluator.evaluate(
        expected=expected,
        observed=observed,
    )

    expected["throughput"] = 999
    observed["throughput"] = 999

    assert result["expected"]["throughput"] == 100
    assert result["observed"]["throughput"] == 110


def test_evaluator_has_no_execution_or_memory_interface():
    evaluator = OutcomeEvaluator()

    assert not hasattr(evaluator, "executor")
    assert not hasattr(evaluator, "execute")
    assert not hasattr(evaluator, "decision_memory")
    assert not hasattr(evaluator, "learning_engine")
