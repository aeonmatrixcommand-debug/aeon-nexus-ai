from src.platform.global_scale.region_manager import (
    RegionManager,
)

from src.platform.global_scale.tenant_isolation import (
    TenantIsolation,
)

from src.platform.global_scale.sla_monitor import (
    SLAMonitor,
)


def test_region():

    region = RegionManager().register(
        "asia-pacific",
    )

    result = RegionManager().health(
        region,
    )

    assert result["available"]


def test_isolation():

    result = TenantIsolation().validate(
        "customer001",
        "tenant-space",
    )

    assert result["isolated"]


def test_sla():

    result = SLAMonitor().evaluate(
        99.9,
        99.0,
    )

    assert result["meeting_sla"]
