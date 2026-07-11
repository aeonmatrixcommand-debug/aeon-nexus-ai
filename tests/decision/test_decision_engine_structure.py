from pathlib import Path

def test_decision_engine_structure():
    required = [
        "docs/decision",
        "services/guardian/decision_engine",
        "tests/decision",
    ]
    for item in required:
        assert Path(item).exists()
