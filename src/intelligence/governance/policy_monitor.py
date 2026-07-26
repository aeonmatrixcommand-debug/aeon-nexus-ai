"""
AEON MATRIX Policy Violation Monitor
Sprint 82
"""


class PolicyMonitor:

    def check(
        self,
        action,
        approved,
    ):

        return {
            "action": action,
            "violation": not approved,
            "blocked": not approved,
        }
