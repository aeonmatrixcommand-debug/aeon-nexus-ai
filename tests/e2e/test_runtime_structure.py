from pathlib import Path

MODULES = [
    "services/guardian",
    "docs",
    "tests",
]

def test_runtime_structure():
    for module in MODULES:
        assert Path(module).exists()
