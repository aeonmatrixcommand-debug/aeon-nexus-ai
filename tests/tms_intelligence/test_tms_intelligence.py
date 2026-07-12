from services.guardian.tms_intelligence.runtime import TMSIntelligence


def test_route():
    assert TMSIntelligence().analyze_route(
        {"distance": 100}
    )["route_status"] == "optimized"
