from services.guardian.event_processing.event_processor import EventProcessor

def test_event_processor():
    processor = EventProcessor()
    result = processor.process({
        "type": "inventory.updated",
        "warehouse": "WH-001"
    })

    assert result["status"] == "processed"
    assert result["event_type"] == "inventory.updated"
