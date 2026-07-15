
from services.agents.observability.agent_telemetry import (
    AgentTelemetryCollector
)


def test_record_execution():

    telemetry = AgentTelemetryCollector()

    telemetry.record_execution(
        "wms-agent",
        "task-001",
        True
    )

    metrics = telemetry.get_agent_metrics(
        "wms-agent"
    )

    assert metrics["executions"] == 1
    assert metrics["success_rate"] == 1



def test_record_error():

    telemetry = AgentTelemetryCollector()

    telemetry.record_error(
        "sales-agent",
        "timeout"
    )

    assert len(
        telemetry.events
    ) == 1



def test_record_latency():

    telemetry = AgentTelemetryCollector()

    telemetry.record_latency(
        "forecast-agent",
        120
    )

    assert telemetry.events[0]["latency_ms"] == 120

