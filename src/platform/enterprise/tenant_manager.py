"""
AEON MATRIX Enterprise Tenant Manager
Sprint 89
"""


from dataclasses import dataclass


@dataclass
class Tenant:

    tenant_id: str
    name: str
    status: str


class TenantManager:


    def create(
        self,
        tenant_id,
        name,
    ):

        return Tenant(
            tenant_id=tenant_id,
            name=name,
            status="active",
        )


    def suspend(
        self,
        tenant,
    ):

        tenant.status = "suspended"

        return tenant
