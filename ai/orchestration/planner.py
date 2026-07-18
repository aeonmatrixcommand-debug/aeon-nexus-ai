"""
AEON MATRIX Agent Planner
"""

from ai.agents.registry import run_agent


def plan(task, **kwargs):

    mapping = {
        "inventory_check": "inventory_agent",
        "risk_analysis": "risk_agent",
        "demand_forecast": "forecast_agent"
    }

    agent = mapping.get(task)

    if not agent:
        return {
            "error": "unknown_task"
        }

    return run_agent(
        agent,
        **kwargs
    )
