"""
AEON MATRIX Mother Brain Runtime Coordinator
Sprint 79 Intelligence Fusion Layer
"""

from dataclasses import dataclass

from src.intelligence.mother_brain.reasoning_pipeline import (
    ReasoningPipeline,
)

from src.intelligence.mother_brain.decision_engine import (
    DecisionEngine,
    DecisionContext,
)

from src.intelligence.mother_brain.action_orchestrator import (
    ActionOrchestrator,
)


@dataclass
class RuntimeDecision:
    signal: str
    action: str
    confidence: float


class MotherBrainRuntime:
    """
    End-to-end autonomous intelligence runtime.
    """

    def __init__(self):
        self.reasoning = ReasoningPipeline()
        self.decision = DecisionEngine()
        self.action = ActionOrchestrator()

    def process(self, signal: str) -> RuntimeDecision:
        reasoning_result = self.reasoning.analyze(signal)

        decision_result = self.decision.evaluate(
            DecisionContext(
                signal=reasoning_result.hypothesis,
                confidence=reasoning_result.confidence,
            )
        )

        action_result = self.action.execute(
            "autonomous response"
        )

        return RuntimeDecision(
            signal=decision_result["signal"],
            action=action_result.action,
            confidence=reasoning_result.confidence,
        )
