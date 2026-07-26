"""
AEON MATRIX Reliability Monitor
Sprint 87
"""


class ReliabilityMonitor:

    def check(
        self,
        services,
    ):

        failed = [
            service
            for service, status in services.items()
            if not status
        ]

        return {
            "healthy": len(failed) == 0,
            "failed_services": failed,
        }
