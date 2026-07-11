from pathlib import Path

def test_production_structure():
    required = [
        "docs/production",
        "deployment/production",
        "tests/production",
    ]
    for path in required:
        assert Path(path).exists()
