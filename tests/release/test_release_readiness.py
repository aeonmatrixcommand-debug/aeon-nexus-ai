from pathlib import Path

REQUIRED = [
    "deployment",
    "docs/release",
    "tests/release",
]

def test_release_structure():
    for path in REQUIRED:
        assert Path(path).exists()
