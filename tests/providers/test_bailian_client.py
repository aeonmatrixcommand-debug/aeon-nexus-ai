from __future__ import annotations

import subprocess
from unittest.mock import patch

import pytest

from providers.bailian.client import BailianClient


def test_client_success() -> None:
    fake_result = subprocess.CompletedProcess(
        args=[],
        returncode=0,
        stdout='{"content":"hello"}',
        stderr="",
    )

    with patch(
        "providers.bailian.client.subprocess.run",
        return_value=fake_result,
    ):
        response = BailianClient().chat("hello")

    assert response.content == "hello"
    assert response.raw["content"] == "hello"


def test_client_nonzero_exit() -> None:
    fake_result = subprocess.CompletedProcess(
        args=[],
        returncode=1,
        stdout="",
        stderr="model access denied",
    )

    with patch(
        "providers.bailian.client.subprocess.run",
        return_value=fake_result,
    ):
        with pytest.raises(RuntimeError, match="exit code 1"):
            BailianClient().chat("hello")


def test_client_invalid_json() -> None:
    fake_result = subprocess.CompletedProcess(
        args=[],
        returncode=0,
        stdout="not-json",
        stderr="",
    )

    with patch(
        "providers.bailian.client.subprocess.run",
        return_value=fake_result,
    ):
        with pytest.raises(ValueError):
            BailianClient().chat("hello")


def test_client_missing_content() -> None:
    fake_result = subprocess.CompletedProcess(
        args=[],
        returncode=0,
        stdout='{"usage":{"input_tokens":1}}',
        stderr="",
    )

    with patch(
        "providers.bailian.client.subprocess.run",
        return_value=fake_result,
    ):
        with pytest.raises(
            ValueError,
            match="missing string content",
        ):
            BailianClient().chat("hello")
