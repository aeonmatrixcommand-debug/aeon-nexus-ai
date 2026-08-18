"""AEON MATRIX Enterprise Cognitive Digital Twin Runtime.

Canonical governed orchestration layer.

Flow:
Sense -> Think -> Simulate -> Decide -> Govern
      -> Authorize -> Act -> Verify -> Learn
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Iterable, Optional

from digital_twin.world_signal.signal_collector import SignalCollector
from digital_twin.engine.reasoning_engine import ReasoningEngine
from digital_twin.simulation.scenario_simulator import ScenarioSimulator
from digital_twin.governance.policy_engine import PolicyEngine
from digital_twin.governance.approval_engine import ApprovalEngine
from digital_twin.governance.execution_guard import ExecutionGuard
from digital_twin.autonomy.verification_engine import VerificationEngine
from digital_twin.adaptive.learning_engine import LearningEngine


class ECDTExecutionMode(str, Enum):
    """Execution authority granted to the ECDT."""

    DRY_RUN = "DRY_RUN"
    HUMAN_REQUIRED = "HUMAN_REQUIRED"
    EXECUTE = "EXECUTE"


class ECDTRuntime:
    """Governed Enterprise Cognitive Digital Twin orchestrator.

    EXECUTE mode does not itself mutate an enterprise system.
    A concrete executor must be explicitly injected.
    """

    def __init__(
        self,
        *,
        executor: Optional[Any] = None,
        execution_mode: ECDTExecutionMode = ECDTExecutionMode.DRY_RUN,
    ) -> None:
        self.signal_collector = SignalCollector()
        self.reasoning_engine = ReasoningEngine()
        self.scenario_simulator = ScenarioSimulator()
        self.policy_engine = PolicyEngine()
        self.approval_engine = ApprovalEngine()
        self.execution_guard = ExecutionGuard()
        self.verification_engine = VerificationEngine()
        self.learning_engine = LearningEngine()

        self.executor = executor
        self.execution_mode = execution_mode

    def run(
        self,
        *,
        signals: Iterable[Dict[str, Any]],
        risk: Dict[str, Any],
        scenario: Dict[str, Any],
        action: str,
        human_approved: bool = False,
    ) -> Dict[str, Any]:
        """Run one governed cognitive decision cycle."""

        signal_list = list(signals)

        sensed = self.signal_collector.collect(signal_list)
        reasoning = self.reasoning_engine.explain(risk)
        simulation = self.scenario_simulator.simulate(scenario)

        policy = self.policy_engine.check(action)

        trace: Dict[str, Any] = {
            "sense": sensed,
            "think": reasoning,
            "simulate": simulation,
            "action": action,
            "governance": {
                "policy": policy,
            },
            "execution_mode": self.execution_mode.value,
        }

        # Policy denial always wins.
        if not policy.get("allowed", False):
            if policy.get("approval_required", False) and not human_approved:
                approval = self.approval_engine.request(action)
                trace["governance"]["approval"] = approval
                trace["status"] = "HUMAN_REQUIRED"
                trace["executed"] = False
                return trace

            if not human_approved:
                trace["status"] = "BLOCKED"
                trace["executed"] = False
                return trace

        # Human approval is never inferred.
        if policy.get("approval_required", False):
            if not human_approved:
                trace["governance"]["approval"] = (
                    self.approval_engine.request(action)
                )
                trace["status"] = "HUMAN_REQUIRED"
                trace["executed"] = False
                return trace

            trace["governance"]["approval"] = (
                self.approval_engine.approve(action)
            )

        guard = self.execution_guard.validate(action)
        trace["governance"]["execution_guard"] = guard

        # Guard denial cannot be bypassed by human_approved.
        if not guard.get("allowed", False):
            trace["status"] = "BLOCKED"
            trace["executed"] = False
            return trace

        # Default safe mode.
        if self.execution_mode == ECDTExecutionMode.DRY_RUN:
            trace["status"] = "DRY_RUN"
            trace["executed"] = False
            return trace

        if self.execution_mode == ECDTExecutionMode.HUMAN_REQUIRED:
            if not human_approved:
                trace["governance"]["approval"] = (
                    self.approval_engine.request(action)
                )
                trace["status"] = "HUMAN_REQUIRED"
                trace["executed"] = False
                return trace

        # EXECUTE requires an explicit adapter.
        if self.executor is None:
            trace["status"] = "EXECUTOR_REQUIRED"
            trace["executed"] = False
            return trace

        result = self.executor.execute(action)

        trace["execution_result"] = result
        trace["executed"] = True

        verification = self.verification_engine.verify(action, result)
        trace["verification"] = verification

        # Learning occurs only after verification.
        if verification.get("verified", False):
            trace["learning"] = self.learning_engine.learn([trace])
            trace["status"] = "COMPLETED"
        else:
            trace["status"] = "VERIFICATION_FAILED"

        return trace
