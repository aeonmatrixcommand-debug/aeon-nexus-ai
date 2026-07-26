"""
AEON MATRIX Profit Intelligence
Sprint 83
"""


class ProfitOptimizer:

    def evaluate(
        self,
        revenue,
        cost,
    ):

        return {
            "profit": revenue - cost,
            "margin": round(
                (revenue - cost) / revenue,
                2,
            ),
        }
