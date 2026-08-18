import pytest

from src.intelligence.ecdt.learning_candidate import LearningCandidate
from src.intelligence.ecdt.learning_candidate_builder import (
    LearningCandidateBuilder,
)


def sample_candidate() -> LearningCandidate:
    return LearningCandidate(
        source_decision_id="decision-001",
        correlation_id="corr-001",
        evidence={
            "expected": {"throughput": 100},
            "observed": {"throughput": 110},
        },
        observed_delta={"throughput": 10},
        proposed_adjustment={
            "parameter": "capacity_target",
            "direction": "increase",
        },
        confidence=0.84,
    )


def test_candidate_has_identity_and_timestamp():
    candidate = sample_candidate()

    assert candidate.candidate_id
    assert candidate.timestamp
    assert candidate.source_decision_id == "decision-001"
    assert candidate.correlation_id == "corr-001"


def test_candidate_always_requires_review():
    candidate = sample_candidate()

    assert candidate.requires_review is True


def test_candidate_cannot_disable_review():
    with pytest.raises(ValueError):
        LearningCandidate(
            source_decision_id="decision-001",
            correlation_id="corr-001",
            requires_review=False,
        )


def test_confidence_must_be_bounded():
    with pytest.raises(ValueError):
        LearningCandidate(
            source_decision_id="decision-001",
            correlation_id="corr-001",
            confidence=1.01,
        )

    with pytest.raises(ValueError):
        LearningCandidate(
            source_decision_id="decision-001",
            correlation_id="corr-001",
            confidence=-0.01,
        )


def test_to_dict_is_defensive():
    candidate = sample_candidate()

    result = candidate.to_dict()
    result["evidence"]["expected"]["throughput"] = 999
    result["proposed_adjustment"]["direction"] = "mutated"

    stored = candidate.to_dict()

    assert stored["evidence"]["expected"]["throughput"] == 100
    assert stored["proposed_adjustment"]["direction"] == "increase"


def test_input_mutation_does_not_change_candidate():
    evidence = {
        "expected": {"throughput": 100},
    }

    adjustment = {
        "direction": "increase",
    }

    candidate = LearningCandidate(
        source_decision_id="decision-001",
        correlation_id="corr-001",
        evidence=evidence,
        proposed_adjustment=adjustment,
        confidence=0.8,
    )

    evidence["expected"]["throughput"] = 999
    adjustment["direction"] = "decrease"

    result = candidate.to_dict()

    assert result["evidence"]["expected"]["throughput"] == 100
    assert result["proposed_adjustment"]["direction"] == "increase"


def test_builder_preserves_decision_identity():
    builder = LearningCandidateBuilder()

    candidate = builder.build(
        source_decision_id="decision-777",
        correlation_id="corr-777",
        evaluation={
            "delta": {
                "throughput": 10,
            },
        },
        proposed_adjustment={
            "parameter": "capacity_target",
        },
        confidence=0.91,
    )

    assert candidate.source_decision_id == "decision-777"
    assert candidate.correlation_id == "corr-777"
    assert candidate.requires_review is True


def test_builder_extracts_delta():
    builder = LearningCandidateBuilder()

    candidate = builder.build(
        source_decision_id="decision-001",
        correlation_id="corr-001",
        evaluation={
            "delta": {
                "throughput": 10,
            },
        },
        proposed_adjustment={
            "direction": "increase",
        },
        confidence=0.75,
    )

    result = candidate.to_dict()

    assert result["observed_delta"]["throughput"] == 10


def test_builder_requires_source_decision():
    builder = LearningCandidateBuilder()

    with pytest.raises(ValueError):
        builder.build(
            source_decision_id="",
            correlation_id="corr-001",
            evaluation={},
            proposed_adjustment={},
            confidence=0.5,
        )


def test_builder_requires_correlation_id():
    builder = LearningCandidateBuilder()

    with pytest.raises(ValueError):
        builder.build(
            source_decision_id="decision-001",
            correlation_id="",
            evaluation={},
            proposed_adjustment={},
            confidence=0.5,
        )


def test_builder_has_no_execution_memory_or_learning_interface():
    builder = LearningCandidateBuilder()

    assert not hasattr(builder, "executor")
    assert not hasattr(builder, "execute")
    assert not hasattr(builder, "decision_memory")
    assert not hasattr(builder, "learning_engine")
    assert not hasattr(builder, "policy_engine")
