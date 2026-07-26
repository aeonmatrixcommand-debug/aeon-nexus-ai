"""
AEON MATRIX Decision Trace Intelligence
Sprint 80
"""


class DecisionTrace:

    def record(
        self,
        decision,
        confidence,
    ):

        return {
            "decision": decision,
            "confidence": confidence,
            "explainable": True,
        }
