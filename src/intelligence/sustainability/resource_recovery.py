"""
AEON MATRIX Resource Recovery Intelligence
Sprint 84
"""


class ResourceRecovery:

    def calculate(
        self,
        waste,
        recovered,
    ):

        return {
            "recovery_rate": round(
                recovered / waste,
                2,
            ),
            "improvement_available":
                recovered < waste,
        }
