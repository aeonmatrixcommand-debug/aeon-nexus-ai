from pathlib import Path

def test_enterprise_usecase():
    required = [
        "docs/usecase",
        "services/guardian/usecase",
        "tests/e2e",
    ]
    for item in required:
        assert Path(item).exists()
