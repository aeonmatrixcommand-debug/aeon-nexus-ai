"""Governed read-only evaluation of ECDT decision outcomes.

This module compares expected numeric outcomes with observed outcomes.
It performs analysis only: no execution, policy mutation, memory writes,
or autonomous learning.
"""

from copy import deepcopy
from typing import Any, Dict, Mapping


class OutcomeEvaluator:
    """Compare expected and observed decision outcomes safely."""

    def evaluate(
        self,
        *,
        expected: Mapping[str, Any],
        observed: Mapping[str, Any],
    ) -> Dict[str, Any]:
        """Return a read-only-style evaluation snapshot."""

        expected_copy = deepcopy(dict(expected))
        observed_copy = deepcopy(dict(observed))

        metrics: Dict[str, Dict[str, Any]] = {}

        shared_keys = expected_copy.keys() & observed_copy.keys()

        for key in sorted(shared_keys):
            expected_value = expected_copy[key]
            observed_value = observed_copy[key]

            if not self._is_numeric(expected_value):
                continue

            if not self._is_numeric(observed_value):
                continue

            variance = observed_value - expected_value

            if expected_value == 0:
                variance_percent = None
            else:
                variance_percent = (
                    variance / abs(expected_value)
                ) * 100.0

            metrics[key] = {
                "expected": expected_value,
                "observed": observed_value,
                "variance": variance,
                "absolute_variance": abs(variance),
                "variance_percent": variance_percent,
            }

        return {
            "evaluation": True,
            "executable": False,
            "expected": expected_copy,
            "observed": observed_copy,
            "metrics": metrics,
            "metric_count": len(metrics),
        }

    @staticmethod
    def _is_numeric(value: Any) -> bool:
        """Accept real int/float metrics but reject booleans."""
        return (
            isinstance(value, (int, float))
            and not isinstance(value, bool)
        )
