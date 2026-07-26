from src.intelligence.resource.resource_intelligence import (
    ResourceIntelligence,
)

from src.intelligence.warehouse.capacity_engine import (
    CapacityEngine,
)

from src.intelligence.fleet.cost_optimizer import (
    FleetCostOptimizer,
)

from src.intelligence.sustainability.resource_recovery import (
    ResourceRecovery,
)

from src.intelligence.simulation.business_impact import (
    BusinessImpactSimulator,
)


def test_resource_assessment():

    result = ResourceIntelligence().assess(
        "warehouse",
        0.8,
        0.9,
    )

    assert result.efficiency == 0.9


def test_capacity():

    result = CapacityEngine().analyze(
        900,
        1000,
    )

    assert result["overflow_risk"]


def test_fleet_cost():

    result = FleetCostOptimizer().evaluate(
        100,
        50,
        30,
    )

    assert result["total_cost"] == 180


def test_resource_recovery():

    result = ResourceRecovery().calculate(
        100,
        40,
    )

    assert result["recovery_rate"] == 0.4


def test_business_impact():

    result = BusinessImpactSimulator().simulate(
        200,
        100,
    )

    assert result["positive"]
