from pathlib import Path

CORE_COMPONENTS = [
    "services",
    "docs",
    "tests"
]

def test_core_components_exist():
    for component in CORE_COMPONENTS:
        assert Path(component).exists()
