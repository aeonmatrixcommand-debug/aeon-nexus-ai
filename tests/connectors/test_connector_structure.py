from pathlib import Path

def test_connector_structure():
    required = [
        "services/guardian/connectors",
        "docs/connectors",
        "tests/connectors",
    ]
    for item in required:
        assert Path(item).exists()
