from services.agents.kpi.agent_kpi import AgentKPI


def test_agent_kpi_record_execution():

    kpi = AgentKPI()

    kpi.record_execution(
        agent_name="WMS_AGENT",
        success=True,
        latency_ms=120,
        business_value=50
    )

    score = kpi.get_score("WMS_AGENT")

    assert score["execution_count"] == 1
    assert score["success_rate"] == 1.0


def test_agent_kpi_failure_tracking():

    kpi = AgentKPI()

    kpi.record_execution(
        agent_name="RISK_AGENT",
        success=False,
        latency_ms=500,
        business_value=0
    )

    score = kpi.get_score("RISK_AGENT")

    assert score["execution_count"] == 1
    assert score["success_rate"] == 0


def test_agent_kpi_latency_measurement():

    kpi = AgentKPI()

    kpi.record_execution(
        agent_name="LANGUAGE_AGENT",
        success=True,
        latency_ms=200
    )

    kpi.record_execution(
        agent_name="LANGUAGE_AGENT",
        success=True,
        latency_ms=300
    )

    score = kpi.get_score("LANGUAGE_AGENT")

    assert score["average_latency_ms"] == 250
