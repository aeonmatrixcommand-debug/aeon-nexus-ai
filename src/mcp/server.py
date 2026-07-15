from mcp.registry import MCPRegistry
from mcp.tools.twin_tools import (
    get_twin_state,
    simulate_risk
)
from mcp.tools.governance_tools import (
    request_approval,
    validate_policy
)


class MCPServer:
    """
    AEON MATRIX MCP Runtime Server
    """

    def __init__(self):
        self.registry = MCPRegistry()

        self.register_tools()

    def register_tools(self):

        self.registry.register(
            "get_twin_state",
            get_twin_state,
            "Read Digital Twin current state"
        )

        self.registry.register(
            "simulate_risk",
            simulate_risk,
            "Run risk simulation"
        )

        self.registry.register(
            "request_approval",
            request_approval,
            "Human approval workflow"
        )

        self.registry.register(
            "validate_policy",
            validate_policy,
            "Governance policy validation"
        )


    def execute(self, tool, payload):

        return self.registry.execute(
            tool,
            payload
        )


if __name__ == "__main__":

    server = MCPServer()

    print(
        "AEON MATRIX MCP Runtime ONLINE"
    )

    print(
        server.registry.list_tools()
    )

    print(
        server.execute(
            "get_twin_state",
            {
                "entity":"warehouse_dc01"
            }
        )
    )
