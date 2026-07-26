from services.agent.orchestration.orchestrator import (
    AgentOrchestrator,
    AgentTask,
)


def test_agent_orchestration_dispatch():
    orchestrator = AgentOrchestrator()

    orchestrator.register_agent("AEON-001")

    task = AgentTask(
        agent_id="AEON-001",
        intent="analyze_inventory",
        payload={"warehouse": "WH-01"},
    )

    result = orchestrator.dispatch(task)

    assert result["status"] == "accepted"
    assert result["agent_id"] == "AEON-001"
