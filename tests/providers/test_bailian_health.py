from __future__ import annotations

import subprocess
from unittest.mock import patch

from providers.bailian.health import BailianHealthProbe


def test_health_probe_success() -> None:
    fake_result = subprocess.CompletedProcess(
        args=[],
        returncode=0,
        stdout='{"content":"RUNTIME_OK"}',
        stderr="",
    )

    with patch(
        "providers.bailian.health.subprocess.run",
        return_value=fake_result,
    ):
        snapshot = BailianHealthProbe().run()

    assert snapshot.runtime_call == "success"
    assert snapshot.exit_code == 0
    assert snapshot.evidence_status == "OBSERVED"
    assert snapshot.latency_ms is not None


def test_health_probe_failure_on_nonzero_exit() -> None:
    fake_result = subprocess.CompletedProcess(
        args=[],
        returncode=1,
        stdout="",
        stderr="model access denied",
    )

    with patch(
        "providers.bailian.health.subprocess.run",
        return_value=fake_result,
    ):
        snapshot = BailianHealthProbe().run()

    assert snapshot.runtime_call == "failed"
    assert snapshot.exit_code == 1
    assert snapshot.evidence_status == "OBSERVED"
    assert snapshot.stderr == "model access denied"


def test_health_probe_failure_without_runtime_token() -> None:
    fake_result = subprocess.CompletedProcess(
        args=[],
        returncode=0,
        stdout='{"content":"unexpected"}',
        stderr="",
    )

    with patch(
        "providers.bailian.health.subprocess.run",
        return_value=fake_result,
    ):
        snapshot = BailianHealthProbe().run()

    assert snapshot.runtime_call == "failed"
    assert snapshot.exit_code == 0


def test_health_probe_timeout() -> None:
    with patch(
        "providers.bailian.health.subprocess.run",
        side_effect=subprocess.TimeoutExpired(cmd=["bl"], timeout=30),
    ):
        snapshot = BailianHealthProbe().run()

    assert snapshot.runtime_call == "failed"
    assert snapshot.exit_code is None
    assert snapshot.stderr == "timeout"
