"""Deterministic, side-effect-free scenario evaluation for AEON MATRIX ECDT."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping, Sequence, Tuple


@dataclass(frozen=True)
class ScenarioEvaluation:
    name: str
    score: float
    rank: int
    status: str
    metrics: Mapping[str, float]
    trace: Tuple[str, ...]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "score": self.score,
            "rank": self.rank,
            "status": self.status,
            "metrics": dict(self.metrics),
            "trace": list(self.trace),
        }


class ECDTScenarioEngine:
    """Evaluate and rank candidate scenarios without executing any action."""

    def evaluate(
        self,
        *,
        observed_state: Mapping[str, Any],
        scenarios: Sequence[Mapping[str, Any]],
        policy: Mapping[str, Any] | None = None,
    ) -> Dict[str, Any]:
        if observed_state is None:
            raise ValueError("observed_state is required")

        if not scenarios:
            raise ValueError("at least one scenario is required")

        allowed = True if policy is None else bool(policy.get("allowed", True))

        evaluations = [
            self._evaluate_one(
                observed_state=observed_state,
                scenario=scenario,
                allowed=allowed,
            )
            for scenario in scenarios
        ]

        ranked = sorted(
            evaluations,
            key=lambda item: (-item["score"], item["name"]),
        )

        results = []
        for index, item in enumerate(ranked, start=1):
            result = ScenarioEvaluation(
                name=item["name"],
                score=item["score"],
                rank=index,
                status=item["status"],
                metrics=item["metrics"],
                trace=item["trace"],
            )
            results.append(result.to_dict())

        recommended = next(
            (
                item
                for item in results
                if item["status"] == "ELIGIBLE"
            ),
            None,
        )

        return {
            "status": "EVALUATED",
            "executed": False,
            "scenario_count": len(results),
            "recommended": recommended,
            "results": results,
            "governance": {
                "policy_allowed": allowed,
                "execution_authorized": False,
            },
        }

    def _evaluate_one(
        self,
        *,
        observed_state: Mapping[str, Any],
        scenario: Mapping[str, Any],
        allowed: bool,
    ) -> Dict[str, Any]:
        name = str(scenario.get("name", "")).strip()
        if not name:
            raise ValueError("scenario name is required")

        impact = self._as_float(
            scenario.get("impact_score", 0.0),
        )
        risk = self._as_float(
            scenario.get("risk_score", 0.0),
        )
        confidence = self._as_float(
            scenario.get("confidence", 1.0),
        )

        score = round(
            (impact * confidence) - risk,
            6,
        )

        status = "ELIGIBLE" if allowed else "POLICY_BLOCKED"

        trace = (
            f"scenario={name}",
            f"impact_score={impact}",
            f"risk_score={risk}",
            f"confidence={confidence}",
            f"policy_allowed={allowed}",
            f"observed_keys={','.join(sorted(map(str, observed_state.keys())))}",
        )

        return {
            "name": name,
            "score": score,
            "status": status,
            "metrics": {
                "impact_score": impact,
                "risk_score": risk,
                "confidence": confidence,
            },
            "trace": trace,
        }

    @staticmethod
    def _as_float(value: Any) -> float:
        try:
            return float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError("scenario metric must be numeric") from exc
