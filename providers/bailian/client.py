from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass


@dataclass(frozen=True)
class BailianResponse:
    content: str
    raw: dict


class BailianClient:
    def __init__(
        self,
        *,
        endpoint: str = "https://dashscope-intl.aliyuncs.com/api/v1",
        model: str = "qwen3.8-max",
        timeout_seconds: int = 60,
    ) -> None:
        self.endpoint = endpoint
        self.model = model
        self.timeout_seconds = timeout_seconds

    def chat(self, message: str, system: str | None = None) -> BailianResponse:
        command = [
            "bl",
            "text",
            "chat",
            "--base-url",
            self.endpoint,
            "--model",
            self.model,
            "--message",
            message,
            "--output",
            "json",
        ]

        if system:
            command.extend(["--system", system])

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=self.timeout_seconds,
            check=False,
        )

        if result.returncode != 0:
            raise RuntimeError(
                f"Bailian CLI failed with exit code {result.returncode}: "
                f"{result.stderr.strip()}"
            )

        payload = json.loads(result.stdout)
        content = payload.get("content")

        if not isinstance(content, str):
            raise ValueError("Bailian response missing string content")

        return BailianResponse(
            content=content,
            raw=payload,
        )
