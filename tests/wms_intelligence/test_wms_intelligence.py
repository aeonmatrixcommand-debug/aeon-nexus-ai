from services.guardian.wms_intelligence.runtime import WMSIntelligence


def test_wms_event():
    assert WMSIntelligence().process_event(
        {"type": "pick_completed"}
    )["validated"]
