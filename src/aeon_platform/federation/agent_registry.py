"""
AEON MATRIX Partner Agent Registry
Sprint 94
"""


from dataclasses import dataclass


@dataclass
class PartnerAgent:

    name: str
    organization: str
    status: str


class AgentRegistry:


    def register(
        self,
        name,
        organization,
    ):

        return PartnerAgent(
            name=name,
            organization=organization,
            status="trusted",
        )


    def lookup(
        self,
        agent,
    ):

        return {
            "name": agent.name,
            "organization": agent.organization,
            "trusted":
                agent.status == "trusted",
        }
