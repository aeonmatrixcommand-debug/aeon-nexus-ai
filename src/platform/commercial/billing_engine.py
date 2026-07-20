"""
AEON MATRIX SaaS Billing Engine
Sprint 91
"""


class BillingEngine:


    def calculate(
        self,
        usage,
        rate,
    ):

        return {
            "usage": usage,
            "rate": rate,
            "amount": usage * rate,
        }
