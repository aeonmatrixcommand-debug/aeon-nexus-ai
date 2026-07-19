from services.guardian.executive_stream.decision_feed import ExecutiveDecisionFeed
from services.guardian.executive_stream.kpi_engine import ExecutiveKPIEngine


def test_executive_live_stream():

    feed = ExecutiveDecisionFeed()

    event = {
        "module": "DemandForecast",
        "decision": "OPTIMIZE_ALLOCATION",
        "confidence": 0.94,
        "risk_score": 0.1,
    }

    record = feed.consume(event)

    assert record["status"] == "ACTIVE"

    kpi = ExecutiveKPIEngine().calculate(event)

    assert kpi["AI_CONFIDENCE"] == 0.94
    assert kpi["DECISION_HEALTH"] == "GREEN"
