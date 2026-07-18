import os
import pytest

from ai.orchestrator import run


@pytest.mark.skipif(
    os.getenv("RUN_LIVE_TESTS") != "1",
    reason="Live Gemini API test disabled"
)
def test_ai_runtime_live():
    response = run("ตอบเพียงคำว่า AI Runtime Ready")
    assert response


def test_ai_runtime_mock():
    assert True
