from services.guardian.kpi_intelligence.runtime import KPIIntelligenceEngine


def test_kpi_intelligence():
    result = KPIIntelligenceEngine().evaluate(
        {"otif": 98, "sla": 97}
    )

    assert result["otif_status"] == "healthy"

    result = KPIIntelligenceEngine().evaluate(
        {"otif": 80, "sla": 90}
    )

    assert result["sla_status"] == "risk"
