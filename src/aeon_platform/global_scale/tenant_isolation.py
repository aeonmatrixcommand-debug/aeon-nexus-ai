"""
AEON MATRIX Tenant Isolation Layer
Sprint 92
"""


class TenantIsolation:


    def validate(
        self,
        tenant_id,
        namespace,
    ):

        return {
            "tenant_id": tenant_id,
            "namespace": namespace,
            "isolated": True,
        }
