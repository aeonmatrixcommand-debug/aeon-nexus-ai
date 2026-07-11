from pathlib import Path

def test_operational_feedback():
    required = [
        "docs/operations",
        "services/guardian/operational_feedback",
        "tests/operational"
    ]

    for path in required:
        assert Path(path).exists()
