"""
AEON MATRIX Resource Allocation Intelligence
Sprint 83
"""


class AllocationEngine:

    def allocate(
        self,
        demand,
        capacity,
    ):

        utilization = round(
            demand / capacity,
            2,
        )

        return {
            "demand": demand,
            "capacity": capacity,
            "utilization": utilization,
            "balanced": utilization <= 1,
        }
