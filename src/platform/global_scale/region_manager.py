"""
AEON MATRIX Multi Region Manager
Sprint 92
"""


from dataclasses import dataclass


@dataclass
class Region:

    name: str
    status: str


class RegionManager:


    def register(
        self,
        name,
    ):

        return Region(
            name=name,
            status="active",
        )


    def health(
        self,
        region,
    ):

        return {
            "region": region.name,
            "available": region.status == "active",
        }
