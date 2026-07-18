import os
import pytest

from ai.orchestrator import run


def test_ai_runtime_mock():
    response = run("AI Runtime Ready")
    assert response


@pytest.mark.skipif(
    os.getenv("RUN_LIVE_TESTS") != "1",
    reason="Live Gemini API test disabled"
)
def test_ai_runtime_live():
    response = run("ตอบเพียงคำว่า AI Runtime Ready")
    assert response
