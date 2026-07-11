from services.guardian.kpi_engine.kpi_engine import KPIEngine

def test_kpi_engine():
    engine = KPIEngine()
    result = engine.calculate({
        "otif": 98,
        "sla": 99,
        "inventory_accuracy": 99.8,
        "fleet_utilization": 87,
        "eta_accuracy": 96,
    })
    assert result["otif"] == 98
    assert result["sla"] == 99
