"""
AEON MATRIX Business Impact Simulation
Sprint 84
"""


class BusinessImpactSimulator:

    def simulate(
        self,
        saving,
        investment,
    ):

        return {
            "roi": round(
                saving / investment,
                2,
            ),
            "positive":
                saving > investment,
        }
