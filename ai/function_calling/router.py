"""
AEON MATRIX Function Calling Router
"""

from ai.tools.enterprise_tools import TOOLS


def execute_tool(name, **kwargs):
    if name not in TOOLS:
        return {
            "error": "tool_not_found",
            "tool": name
        }

    return TOOLS[name](**kwargs)
