"""
AEON MATRIX Warehouse Capacity Intelligence
Sprint 84
"""


class CapacityEngine:

    def analyze(
        self,
        inventory_volume,
        max_capacity,
    ):

        ratio = round(
            inventory_volume / max_capacity,
            2,
        )

        return {
            "capacity_ratio": ratio,
            "overflow_risk": ratio > 0.85,
        }
