from datetime import datetime


class DecisionContract:

    @staticmethod
    def advisory(*, reason, mode, analysis=None):
        """Construct data only; never infer authority from model output."""
        if mode not in {"READ_ONLY", "SIMULATION_ONLY"}:
            raise ValueError("advisory_mode_required")
        result = {
            "status": "PROPOSED" if analysis is not None else "NO_DECISION",
            "reason": reason, "mode": mode,
            "execution_authorized": False, "executed": False,
        }
        if analysis is not None:
            result["analysis"] = {
                "summary": analysis["summary"],
                "evidence_ids": list(analysis["evidence_ids"]),
            }
        else:
            result["axiom"] = "No Evidence -> No Decision"
        return result

    def __init__(
        self,
        decision="PENDING",
        confidence=0.0,
        reason=None
    ):
        self.decision = decision
        self.confidence = confidence
        self.reason = reason
        self.timestamp = datetime.utcnow().isoformat()


    def to_dict(self):
        return {
            "decision": self.decision,
            "confidence": self.confidence,
            "reason": self.reason,
            "timestamp": self.timestamp
        }
