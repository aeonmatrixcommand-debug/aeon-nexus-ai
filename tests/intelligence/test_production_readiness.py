from src.intelligence.production.security_gate import (
    SecurityGate,
)

from src.intelligence.production.reliability_monitor import (
    ReliabilityMonitor,
)

from src.intelligence.production.performance_validator import (
    PerformanceValidator,
)

from src.intelligence.production.release_gate import (
    ReleaseGate,
)


def test_security():

    result = SecurityGate().validate(
        True,
        True,
    )

    assert result["approved"]


def test_reliability():

    result = ReliabilityMonitor().check(
        {
            "api": True,
            "database": True,
        }
    )

    assert result["healthy"]


def test_performance():

    result = PerformanceValidator().evaluate(
        100,
        200,
    )

    assert result["within_target"]


def test_release_gate():

    result = ReleaseGate().approve(
        True,
        True,
        True,
    )

    assert result["release_ready"]
