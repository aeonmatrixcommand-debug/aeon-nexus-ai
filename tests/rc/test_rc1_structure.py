from pathlib import Path

REQUIRED = [
    "release",
    "docs/release",
    "tests/rc",
]

def test_rc_structure():
    for item in REQUIRED:
        assert Path(item).exists()
