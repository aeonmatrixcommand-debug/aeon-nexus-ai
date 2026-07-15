from services.agents.core.capability import AgentCapability
from services.agents.core.task import AgentTask
from services.agents.core.message import AgentMessage
from services.agents.core.result import AgentResult


def test_agent_capability_contract():

    capability = AgentCapability(
        name="inventory_check",
        domain="warehouse",
        risk_level="medium"
    )

    assert capability.name == "inventory_check"
    assert capability.domain == "warehouse"
    assert capability.risk_level == "medium"


def test_agent_task_contract():

    task = AgentTask(
        task_id="task-001",
        capability="inventory_check",
        payload={
            "sku": "A100"
        }
    )

    assert task.task_id == "task-001"
    assert task.capability == "inventory_check"
    assert task.payload["sku"] == "A100"


def test_agent_message_contract():

    message = AgentMessage(
        sender="demand_agent",
        receiver="inventory_agent",
        message_type="REQUEST",
        payload={
            "forecast": "increase"
        }
    )

    assert message.sender == "demand_agent"
    assert message.receiver == "inventory_agent"
    assert message.message_type == "REQUEST"


def test_agent_result_contract():

    result = AgentResult(
        success=True,
        agent_name="wms_agent",
        output={
            "status": "completed"
        }
    )

    assert result.success is True
    assert result.agent_name == "wms_agent"
    assert result.output["status"] == "completed"
