from src.platform.enterprise.tenant_manager import (
    TenantManager,
)

from src.platform.enterprise.deployment_manager import (
    DeploymentManager,
)

from src.platform.enterprise.usage_meter import (
    UsageMeter,
)


def test_tenant_creation():

    tenant = TenantManager().create(
        "customer001",
        "Enterprise Customer",
    )

    assert tenant.status == "active"


def test_deployment():

    result = DeploymentManager().validate(
        "production",
        True,
    )

    assert result["deployable"]


def test_usage():

    result = UsageMeter().calculate(
        [
            "order",
            "inventory",
            "delivery",
        ]
    )

    assert result["usage_score"] == 3
