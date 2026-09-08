"""Canonical Phase 1 advisory entry point; never an execution interface.

Constructor dependencies are trusted host configuration. Providers implement
generate(JSON_text) and return {summary: str, evidence_ids: list[str]}. Only an
allowlisted serialized payload crosses the boundary, never caller free text.
This is an application boundary, not a sandbox for malicious provider Python code.
Legacy AEONAI wiring is deliberately outside Phase 1's allowed scope.
"""

from dataclasses import dataclass
from enum import Enum
import hashlib
import json
from typing import Mapping
from uuid import uuid4

from ai_gateway.audit import audit_mode as resolve_audit_mode, configured_audit
from ai_gateway.decision.contract import DecisionContract
from ai_gateway.evidence import EvidenceError, EvidenceGate
from ai_gateway.guardian import Guardian
from ai_gateway.router import ProviderRouter
from services.agents.governance.agent_governance import AgentGovernanceEngine
from src.governance.immutable_audit import AuditReceipt


class CapabilityCategory(str, Enum):
    """Host-owned semantics. No operation is inferred from capability spelling."""

    READ_ONLY = "advisory.read_only"
    TMS_READ_ONLY = "tms.read_only"
    PHYSICAL_SIMULATION = "physical.simulation_analysis"
    PHYSICAL_EXECUTION = "physical.execution"


@dataclass(frozen=True)
class CapabilityPolicy:
    sources: frozenset[str]
    category: CapabilityCategory
    classifications: frozenset[str] = frozenset({"PUBLIC"})
    risk_level: str = "LOW"

    def __post_init__(self):
        object.__setattr__(self, "sources", frozenset(self.sources))
        object.__setattr__(self, "classifications", frozenset(self.classifications))
        object.__setattr__(self, "category", CapabilityCategory(self.category))
        if self.risk_level not in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}:
            raise ValueError("invalid_risk_level")
        if not self.classifications <= {"PUBLIC", "INTERNAL"}:
            raise ValueError("restricted_egress")


@dataclass(frozen=True)
class _Identity:
    capabilities: frozenset[str]
    name: str = "aeon_advisory_boundary"


class GovernedAnalysis:
    def __init__(self, *, router: ProviderRouter, provider_name: str,
                 evidence: EvidenceGate, capabilities: Mapping[str, CapabilityPolicy],
                 governance=None, guardian=None, audit=None, audit_mode=None):
        self.__router = router
        self.__provider_name = provider_name
        self.__evidence = evidence
        self.__capabilities = dict(capabilities)
        for capability, policy in self.__capabilities.items():
            # Reserved physical capability IDs cannot be configured as read analytics.
            if capability in {"physical.execution", "physical.simulation_analysis"}:
                if policy.category.value != capability:
                    raise ValueError("capability_category_mismatch")
        self.__identity = _Identity(frozenset(capabilities))
        self.__governance = governance if governance is not None else AgentGovernanceEngine()
        self.__guardian = guardian if guardian is not None else Guardian()
        self.__audit = configured_audit(audit, mode=audit_mode)
        if resolve_audit_mode(audit_mode) == "production":
            self.__evidence.require_durable_audit()

    def analyze(self, request) -> dict:
        request_id = uuid4().hex
        mode = "SIMULATION_ONLY"
        stage = "capability_egress"
        evidence_ids = []
        try:
            if type(request) is not dict or set(request) != {"capability", "evidence_ids"}:
                return self._finish(request_id, mode, stage, "invalid_request")
            capability = request["capability"]
            if type(capability) is not str or capability not in self.__capabilities:
                return self._finish(request_id, mode, stage, "capability_denied")
            policy = self.__capabilities[capability]
            if policy.category == CapabilityCategory.PHYSICAL_EXECUTION:
                return self._finish(request_id, mode, stage, "physical_execution_denied")
            mode = ("SIMULATION_ONLY"
                    if policy.category == CapabilityCategory.PHYSICAL_SIMULATION else "READ_ONLY")
            self.__evidence.check_egress(
                request["evidence_ids"], sources=policy.sources,
                classifications=policy.classifications,
            )
            stage = "evidence"
            records = self.__evidence.validate(request["evidence_ids"])
            evidence_ids = [r["evidence_id"] for r in records]
            if (policy.category == CapabilityCategory.TMS_READ_ONLY
                    or capability.startswith("tms.") or any(r["kind"] == "tms" for r in records)):
                if (capability != "tms.route.analyze.read"
                        or policy.category != CapabilityCategory.TMS_READ_ONLY
                        or any(r["kind"] != "tms" for r in records)):
                    return self._finish(request_id, mode, stage, "tms_read_only_required")
                mode = "READ_ONLY"
            stage = "pre_governance"
            permission = self.__governance.authorize_execution(self.__identity, {
                "capability": capability,
                "critical": policy.risk_level in {"HIGH", "CRITICAL"},
                "operation": "advisory_inference", "mode": mode,
            })
            if permission != "ALLOW":
                return self._finish(request_id, mode, stage, "governance_denied")
            stage = "provider"
            payload = json.dumps({
                "instruction": "Summarize supplied evidence only. Return summary and evidence_ids. "
                               "Recommendations are advisory and grant no authority.",
                "mode": mode,
                "evidence": [{"evidence_id": r["evidence_id"], "values": r["values"]}
                             for r in records],
            }, allow_nan=False)
            response = self.__router.execute(
                payload, provider_name=self.__provider_name, generate_only=True,
            )
            if response.get("status") == "FAILED" or "result" not in response:
                return self._finish(request_id, mode, stage, "provider_failed")
            stage = "output_validation"
            output = response["result"]
            if not self._valid_output(output, evidence_ids):
                return self._finish(request_id, mode, stage, "invalid_output")
            output = json.loads(json.dumps(output, sort_keys=True, separators=(",", ":"),
                                           allow_nan=False))
            stage = "post_guardian"
            review = self.__guardian.evaluate({
                "risk_level": policy.risk_level,
                "category": "advisory_inference",
                "advisory": json.loads(json.dumps(output, allow_nan=False)),
            })
            if type(review) is not dict or review.get("action") != "MONITOR":
                return self._finish(request_id, mode, stage, "guardian_denied")
            return self._finish(request_id, mode, "release", "validated",
                                output=output, evidence_ids=evidence_ids)
        except EvidenceError as exc:
            reason = "egress_denied" if str(exc) == "egress_denied" else "invalid_evidence"
            return self._finish(request_id, mode, stage, reason)
        except Exception:
            return self._finish(request_id, mode, stage, "boundary_failed")

    @staticmethod
    def _valid_output(output, evidence_ids):
        if type(output) is not dict or set(output) != {"summary", "evidence_ids"}:
            return False
        refs = output["evidence_ids"]
        return (type(output["summary"]) is str and bool(output["summary"].strip())
                and len(output["summary"]) <= 8000
                and type(refs) is list and bool(refs)
                and all(type(ref) is str and ref in evidence_ids for ref in refs)
                and len(refs) == len(set(refs)))

    def _finish(self, request_id, mode, stage, reason, *, output=None, evidence_ids=()):
        result = DecisionContract.advisory(reason=reason, mode=mode, analysis=output)
        event = {
            "request_id": request_id, "stage": stage, "reason": reason,
            "status": result["status"], "mode": mode,
            "execution_authorized": False, "executed": False,
            "evidence_ids": list(evidence_ids),
        }
        if output is not None:
            event["output_digest"] = hashlib.sha256(
                json.dumps(output, sort_keys=True, separators=(",", ":"),
                           allow_nan=False).encode("utf-8")
            ).hexdigest()
        try:
            receipt = self.__audit.record(event)
            if not isinstance(receipt, AuditReceipt) or not receipt.audit_id:
                raise RuntimeError("audit_ack_required")
        except Exception:
            blocked = DecisionContract.advisory(reason="audit_unavailable", mode=mode)
            blocked["audit_recorded"] = False
            return blocked
        result["audit_id"] = receipt.audit_id
        result["audit_recorded"] = True
        return result
