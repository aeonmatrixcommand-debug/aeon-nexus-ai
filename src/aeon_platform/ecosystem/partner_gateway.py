"""
AEON MATRIX Partner Gateway
Sprint 93
"""


class PartnerGateway:


    def connect(
        self,
        partner,
        service,
    ):

        return {
            "partner": partner,
            "service": service,
            "connected": True,
        }
