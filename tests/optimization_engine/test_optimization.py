from services.guardian.optimization_engine.runtime import OptimizationEngine

def test_optimize():
    assert OptimizationEngine().optimize("flow")["optimized"]
