from src.intelligence.mother_brain.decision_engine import (
    DecisionEngine,
    DecisionContext,
)

from src.intelligence.mother_brain.reasoning_pipeline import (
    ReasoningPipeline,
)

from src.intelligence.mother_brain.action_orchestrator import (
    ActionOrchestrator,
)


def test_mother_brain_flow():

    reasoning = ReasoningPipeline()
    result = reasoning.analyze("inventory risk detected")

    assert result.hypothesis

    decision = DecisionEngine().evaluate(
        DecisionContext(
            signal=result.hypothesis,
            confidence=0.8,
        )
    )

    assert decision["signal"]

    action = ActionOrchestrator().execute(
        "optimize inventory allocation"
    )

    assert action.status == "queued"
