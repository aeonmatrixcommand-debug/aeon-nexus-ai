from services.guardian.executive_api.api import ExecutiveAPI

def test_health():
    api = ExecutiveAPI()
    assert api.health()["status"] == "healthy"

def test_kpi():
    api = ExecutiveAPI()
    result = api.kpi()
    assert "otif" in result
