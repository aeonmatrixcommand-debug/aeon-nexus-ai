"""
AEON MATRIX Capability Registry
Sprint 93
"""


from dataclasses import dataclass


@dataclass
class Capability:

    name: str
    provider: str
    status: str


class CapabilityRegistry:


    def register(
        self,
        name,
        provider,
    ):

        return Capability(
            name=name,
            provider=provider,
            status="active",
        )


    def discover(
        self,
        capability,
    ):

        return {
            "name": capability.name,
            "provider": capability.provider,
            "available": capability.status == "active",
        }
