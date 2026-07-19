"""
AEON MATRIX Agent Registry
Sprint 80
"""

from ai.function_calling.router import execute_tool


AGENTS = {
    "inventory_agent": {
        "tool": "get_inventory"
    },
    "risk_agent": {
        "tool": "analyze_risk"
    },
    "forecast_agent": {
        "tool": "predict_demand"
    }
}


def get_agent(name):
    return AGENTS.get(name)


def run_agent(name, **kwargs):
    agent = get_agent(name)

    if not agent:
        return {
            "error": "agent_not_found",
            "agent": name
        }

    return execute_tool(
        agent["tool"],
        **kwargs
    )
