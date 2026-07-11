from pathlib import Path

def test_recommendation_structure():
    required = [
        "docs/recommendation",
        "services/guardian/recommendation_engine",
        "tests/recommendation",
    ]
    for item in required:
        assert Path(item).exists()
