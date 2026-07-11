from pathlib import Path

def test_observability_structure():
    required = [
        "docs/observability",
        "tests/observability",
        "services/guardian"
    ]
    for path in required:
        assert Path(path).exists()
