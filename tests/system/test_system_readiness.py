from pathlib import Path

def test_core_directories_exist():
    required = [
        "services",
        "docs",
        "tests"
    ]
    for item in required:
        assert Path(item).exists()
