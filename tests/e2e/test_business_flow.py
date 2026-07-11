from pathlib import Path

def test_business_flow_structure():
    required = [
        "docs/validation",
        "scenarios",
        "tests/e2e",
    ]
    for item in required:
        assert Path(item).exists()
