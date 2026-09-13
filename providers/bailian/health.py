from __future__ import annotations

import subprocess
import time
import uuid
from datetime import datetime, timezone

from .models import BailianHealthSnapshot


DEFAULT_ENDPOINT = "https://dashscope-intl.aliyuncs.com/api/v1"
DEFAULT_MODEL = "qwen3.8-max"


class BailianHealthProbe:
    def __init__(
        self,
        *,
        endpoint: str = DEFAULT_ENDPOINT,
        model: str = DEFAULT_MODEL,
        timeout_seconds: int = 30,
    ) -> None:
        self.endpoint = endpoint
        self.model = model
        self.timeout_seconds = timeout_seconds

    def run(self) -> BailianHealthSnapshot:
        request_id = str(uuid.uuid4())

        command = [
            "bl",
            "text",
            "chat",
            "--base-url",
            self.endpoint,
            "--model",
            self.model,
            "--system",
            (
                "Do not invent telemetry. "
                "Reply only with the exact token RUNTIME_OK."
            ),
            "--message",
            f"Health probe request_id={request_id}",
            "--output",
            "json",
        ]

        started = time.perf_counter()

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=self.timeout_seconds,
                check=False,
            )
        except subprocess.TimeoutExpired:
            latency_ms = int((time.perf_counter() - started) * 1000)

            return BailianHealthSnapshot(
                provider="alibaba-bailian",
                model=self.model,
                endpoint=self.endpoint,
                runtime_call="failed",
                exit_code=None,
                latency_ms=latency_ms,
                captured_at=datetime.now(timezone.utc),
                evidence_status="OBSERVED",
                stdout=None,
                stderr="timeout",
            )

        latency_ms = int((time.perf_counter() - started) * 1000)

        stdout = result.stdout.strip() or None
        stderr = result.stderr.strip() or None

        success = (
            result.returncode == 0
            and stdout is not None
            and "RUNTIME_OK" in stdout
        )

        return BailianHealthSnapshot(
            provider="alibaba-bailian",
            model=self.model,
            endpoint=self.endpoint,
            runtime_call="success" if success else "failed",
            exit_code=result.returncode,
            latency_ms=latency_ms,
            captured_at=datetime.now(timezone.utc),
            evidence_status="OBSERVED",
            stdout=stdout,
            stderr=stderr,
        )
