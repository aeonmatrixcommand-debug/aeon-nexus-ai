
from services.guardian.optimization.engine import (
    OptimizationEngine
)


def test_optimizer():

    r=OptimizationEngine().optimize(
        100,
        150,
        160
    )

    assert "action" in r
