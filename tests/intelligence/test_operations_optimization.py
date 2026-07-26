from src.intelligence.optimization.operations_optimizer import (
    OperationsOptimizer,
)

from src.intelligence.resource.allocation_engine import (
    AllocationEngine,
)

from src.intelligence.prediction.sla_predictor import (
    SLAPredictor,
)

from src.intelligence.profit.profit_optimizer import (
    ProfitOptimizer,
)


def test_operations_optimizer():

    result = OperationsOptimizer().optimize(
        "fleet",
        1000,
        800,
    )

    assert result.improvement == 0.2


def test_resource_allocation():

    result = AllocationEngine().allocate(
        80,
        100,
    )

    assert result["balanced"]


def test_sla_prediction():

    result = SLAPredictor().predict(
        0.1,
    )

    assert result["sla_safe"]


def test_profit():

    result = ProfitOptimizer().evaluate(
        1000,
        700,
    )

    assert result["profit"] == 300
