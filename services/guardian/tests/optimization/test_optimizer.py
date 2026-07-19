from services.guardian.optimization.runtime_optimizer import RuntimeOptimizer


def test_optimizer():

    optimizer = RuntimeOptimizer()

    result = optimizer.optimize(
        {
            "confidence": 0.94,
            "agents": [
                {
                    "name": "Forecast",
                    "performance": 90
                },
                {
                    "name": "Risk",
                    "performance": 80
                }
            ]
        }
    )

    assert result["decision"]["decision_score"] == 94
