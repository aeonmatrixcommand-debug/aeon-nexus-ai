from pathlib import Path

def test_dashboard_structure():
    required = [
        "docs/dashboard",
        "services/guardian/executive_dashboard",
        "tests/dashboard",
    ]
    for item in required:
        assert Path(item).exists()
