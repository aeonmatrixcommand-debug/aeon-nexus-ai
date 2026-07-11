from pathlib import Path

REQUIRED = [
    "services/guardian",
    "docs",
    "tests"
]

def test_structure():
    for item in REQUIRED:
        assert Path(item).exists()
