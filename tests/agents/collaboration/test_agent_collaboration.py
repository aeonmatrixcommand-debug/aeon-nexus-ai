from services.agents.collaboration.agent_team import AgentTeam
from services.agents.collaboration.task_delegator import TaskDelegator
from services.agents.collaboration.result_aggregator import ResultAggregator


def test_agent_team_creation():

    team = AgentTeam()

    team.add_agent("WMS_AGENT")
    team.add_agent("TMS_AGENT")

    assert len(team.agents) == 2
    assert "WMS_AGENT" in team.agents


def test_task_delegation():

    delegator = TaskDelegator()

    result = delegator.delegate(
        "inventory_check",
        "WMS_AGENT"
    )

    assert result["agent"] == "WMS_AGENT"
    assert result["task"] == "inventory_check"


def test_result_aggregation():

    aggregator = ResultAggregator()

    aggregator.add_result(
        "WMS_AGENT",
        {
            "stock": 100
        }
    )

    aggregator.add_result(
        "TMS_AGENT",
        {
            "eta": "10:00"
        }
    )

    result = aggregator.combine()

    assert result["WMS_AGENT"]["stock"] == 100
    assert result["TMS_AGENT"]["eta"] == "10:00"
