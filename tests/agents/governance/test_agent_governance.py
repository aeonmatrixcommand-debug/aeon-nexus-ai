
from services.agents.governance.agent_governance import (
    AgentGovernanceEngine
)


class MockAgent:

    name = "wms-agent"

    capabilities = [
        "inventory_check",
        "stock_update"
    ]



def test_governance_allow():

    governance = AgentGovernanceEngine()

    result = governance.authorize_execution(
        MockAgent(),
        {
            "capability": "inventory_check",
            "critical": False
        }
    )

    assert result == "ALLOW"



def test_governance_block_high_risk():

    governance = AgentGovernanceEngine()

    result = governance.authorize_execution(
        MockAgent(),
        {
            "capability": "stock_update",
            "critical": True
        }
    )

    assert result == "BLOCK"



def test_governance_audit():

    governance = AgentGovernanceEngine()

    governance.authorize_execution(
        MockAgent(),
        {
            "capability": "inventory_check"
        }
    )

    assert len(governance.audit_log) == 1

