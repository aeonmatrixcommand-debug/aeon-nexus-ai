from pathlib import Path

def test_mvp_structure():
    required = [
        "docs/mvp",
        "deployment/mvp",
        "tests/mvp",
    ]
    for path in required:
        assert Path(path).exists()
