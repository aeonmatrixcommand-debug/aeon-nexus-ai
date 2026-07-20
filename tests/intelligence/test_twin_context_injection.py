from src.intelligence.digital_twin.context.twin_context import (
    TwinContextAdapter,
)

from src.intelligence.decision.context_bridge import (
    DecisionContextBridge,
)


def test_twin_context_injection():

    context = TwinContextAdapter().inject(
        "warehouse",
        "DC001",
        "capacity_risk",
        0.92,
        {
            "impact": "high"
        },
    )

    decision = DecisionContextBridge().enrich(context)

    assert decision["entity"] == "DC001"
    assert decision["confidence"] == 0.92
    assert decision["simulation"]["impact"] == "high"
