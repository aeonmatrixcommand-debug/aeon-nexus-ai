class MCPRegistry:
    """
    Registry for AEON MATRIX MCP tools.
    """

    def __init__(self):
        self.tools = {}

    def register(self, name, handler, description):
        self.tools[name] = {
            "handler": handler,
            "description": description
        }

    def list_tools(self):
        return list(self.tools.keys())

    def execute(self, name, payload):
        if name not in self.tools:
            return {
                "error": "Tool not found"
            }

        return self.tools[name]["handler"](payload)
