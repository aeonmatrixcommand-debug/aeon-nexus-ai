"""Governed integration between ECDT scenario evaluation and runtime."""

from __future__ import annotations

from typing import Any, Dict, Iterable, Mapping, Sequence

from .runtime import ECDTRuntime
from .scenario_engine import ECDTScenarioEngine


class ECDTGovernedScenarioIntegration:
    """Route a scenario recommendation into ECDTRuntime governance.

    A recommendation is not execution authority.
    All execution decisions remain owned by ECDTRuntime.
    """

    def __init__(
        self,
        *,
        scenario_engine: ECDTScenarioEngine | None = None,
        runtime: ECDTRuntime | None = None,
    ) -> None:
        self.scenario_engine = scenario_engine or ECDTScenarioEngine()
        self.runtime = runtime or ECDTRuntime()

    def run(
        self,
        *,
        signals: Iterable[Dict[str, Any]],
        risk: Dict[str, Any],
        observed_state: Mapping[str, Any],
        scenarios: Sequence[Mapping[str, Any]],
        policy: Mapping[str, Any] | None = None,
        human_approved: bool = False,
    ) -> Dict[str, Any]:
        """Evaluate scenarios, then route the recommendation to governance."""

        evaluation = self.scenario_engine.evaluate(
            observed_state=observed_state,
            scenarios=scenarios,
            policy=policy,
        )

        trace: Dict[str, Any] = {
            "scenario_evaluation": evaluation,
            "recommendation_is_authority": False,
            "executed": False,
        }

        recommendation = evaluation.get("recommended")

        if recommendation is None:
            trace["status"] = "NO_RECOMMENDATION"
            return trace

        selected = self._find_selected_scenario(
            scenarios=scenarios,
            name=str(recommendation["name"]),
        )

        action = str(selected.get("action", "")).strip()
        if not action:
            trace["status"] = "ACTION_REQUIRED"
            trace["selected_scenario"] = dict(selected)
            return trace

        runtime_scenario = selected.get("runtime_scenario")

        if runtime_scenario is None:
            runtime_scenario = {
                "name": recommendation["name"],
            }

        if not isinstance(runtime_scenario, Mapping):
            raise TypeError("runtime_scenario must be mapping-compatible")

        runtime_result = self.runtime.run(
            signals=signals,
            risk=risk,
            scenario=dict(runtime_scenario),
            action=action,
            human_approved=human_approved,
        )

        trace["selected_scenario"] = dict(selected)
        trace["runtime"] = runtime_result
        trace["status"] = runtime_result["status"]
        trace["executed"] = bool(runtime_result.get("executed", False))

        return trace

    @staticmethod
    def _find_selected_scenario(
        *,
        scenarios: Sequence[Mapping[str, Any]],
        name: str,
    ) -> Mapping[str, Any]:
        for scenario in scenarios:
            if str(scenario.get("name", "")).strip() == name:
                return scenario

        raise RuntimeError("recommended scenario not found in source candidates")
