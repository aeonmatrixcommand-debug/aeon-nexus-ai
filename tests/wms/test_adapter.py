from services.guardian.wms_adapter.adapter import WMSAdapter

def test_transform():
    adapter = WMSAdapter()

    event = {
        "event_type": "inventory.updated",
        "warehouse": "WH001",
        "timestamp": "2026-07-11T10:00:00Z"
    }

    result = adapter.transform(event)

    assert result["source"] == "wms"
    assert result["event_type"] == "inventory.updated"
