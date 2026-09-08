"""Phase 1 integration tests. All inference uses the local fake below."""

from datetime import datetime, timedelta, timezone
import hashlib
import json
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from ai_gateway.audit import AuditTrail
from ai_gateway.evidence import EvidenceError, EvidenceGate, EvidenceSource
from ai_gateway.governed_analysis import (
    CapabilityCategory as Category, CapabilityPolicy, GovernedAnalysis,
)
from ai_gateway.guardian import Guardian
from ai_gateway.router import ProviderRouter
from integrations.tms import TMSReadOnlyConnector
from services.agents.governance.agent_governance import AgentGovernanceEngine


NOW = datetime(2026, 9, 8, tzinfo=timezone.utc)
SECRET = "fixture-secret-never-log"


class FakeProvider:
    def __init__(self):
        self.calls = []
        self.transform = lambda output: output

    def generate(self, payload):
        self.calls.append(json.loads(payload))
        return self.transform({
            "summary": "Observed measurement; advisory only.",
            "evidence_ids": [e["evidence_id"] for e in self.calls[-1]["evidence"]],
        })

    def chat(self, *_):
        pytest.fail("No agent chat dispatch is permitted")

    def execute(self, *_):
        pytest.fail("No executor dispatch is permitted")


def make_boundary(*, values=None, required=("distance",), allowed=("distance",),
                  age=0, classification="PUBLIC", kind="telemetry", connector=None,
                  category=Category.READ_ONLY, capability="warehouse.analyze",
                  governance=None, guardian=None, audit=None, reader=None):
    audit = AuditTrail() if audit is None else audit
    reading = {"observed_at": NOW - timedelta(seconds=age),
               "values": {"distance": 100} if values is None else values}
    gate = EvidenceGate({"trusted_source": EvidenceSource(
        reader=reader or (lambda: reading), required_metrics=frozenset(required),
        allowed_metrics=frozenset(allowed), classification=classification, kind=kind,
    )}, clock=lambda: NOW, tms_connector=connector, audit=audit)
    provider = FakeProvider()
    router = ProviderRouter()
    router.register("fake", provider)
    governance = governance if governance is not None else AgentGovernanceEngine()
    guardian = guardian if guardian is not None else Guardian()
    boundary = GovernedAnalysis(
        router=router, provider_name="fake", evidence=gate,
        capabilities={capability: CapabilityPolicy(frozenset({"trusted_source"}), category)},
        governance=governance, guardian=guardian, audit=audit,
    )
    return SimpleNamespace(gate=gate, provider=provider, router=router, boundary=boundary,
                           audit=audit, capability=capability, reading=reading,
                           governance=governance, guardian=guardian)


def request(h, refs=None):
    return {"capability": h.capability,
            "evidence_ids": [h.gate.collect("trusted_source")] if refs is None else refs}


def assert_no_decision(h, result, *, calls=0):
    assert result["status"] == "NO_DECISION"
    assert result["execution_authorized"] is False
    assert result["executed"] is False
    assert "analysis" not in result
    assert len(h.provider.calls) == calls


@pytest.mark.parametrize("values,required,allowed", [
    ({}, ("distance",), ("distance",)),
    ({"weight": 2}, ("distance",), ("distance", "weight")),
    ({"distance": 100}, ("distance", "weight"), ("distance", "weight")),
    ({"distance": 100, "unknown": 2}, ("distance",), ("distance",)),
    ({"distance": float("nan")}, ("distance",), ("distance",)),
    ({"distance": float("inf")}, ("distance",), ("distance",)),
    ({"distance": -float("inf")}, ("distance",), ("distance",)),
    ({"distance": True}, ("distance",), ("distance",)),
    ({"distance": SECRET}, ("distance",), ("distance",)),
])
def test_invalid_collection_is_audited_and_cannot_reach_provider(values, required, allowed):
    h = make_boundary(values=values, required=required, allowed=allowed)
    with pytest.raises(EvidenceError, match="^invalid_evidence$"):
        h.gate.collect("trusted_source")
    event = h.audit.report()[0]["event"]
    assert event["event_type"] == "EVIDENCE_COLLECTION_FAILED"
    assert event["status"] == "NO_DECISION"
    assert_no_decision(h, h.boundary.analyze(request(h, [])))
    assert SECRET not in json.dumps(h.audit.report())


def test_optional_metric_can_be_absent():
    h = make_boundary(allowed=("distance", "weight"))
    assert h.boundary.analyze(request(h))["status"] == "PROPOSED"


@pytest.mark.parametrize("refs", [[], None, ["fabricated"], [{"verified": True}]])
def test_missing_or_fabricated_evidence_zero_calls(refs):
    h = make_boundary()
    assert_no_decision(h, h.boundary.analyze({"capability": h.capability, "evidence_ids": refs}))


@pytest.mark.parametrize("age", [301, -1])
def test_stale_or_future_evidence_zero_calls(age):
    h = make_boundary(age=age)
    assert_no_decision(h, h.boundary.analyze(request(h)))


@pytest.mark.parametrize("classification", ["INTERNAL", "CONFIDENTIAL", "RESTRICTED"])
def test_egress_denied_zero_calls(classification):
    h = make_boundary(classification=classification)
    result = h.boundary.analyze(request(h))
    assert_no_decision(h, result)
    assert result["reason"] == "egress_denied"
    assert h.governance.audit_log == []


def test_unknown_capability_zero_calls():
    h = make_boundary()
    assert_no_decision(h, h.boundary.analyze({**request(h), "capability": "unknown"}))


def test_governance_denial_zero_calls():
    h = make_boundary(governance=SimpleNamespace(authorize_execution=lambda *_: "BLOCK"))
    assert_no_decision(h, h.boundary.analyze(request(h)))


def test_missing_trusted_tms_connector_zero_calls():
    reader = Mock(side_effect=AssertionError("must reject before source access"))
    h = make_boundary(kind="tms", category=Category.TMS_READ_ONLY,
                      capability="tms.route.analyze.read", reader=reader)
    with pytest.raises(EvidenceError, match="^invalid_evidence$"):
        h.gate.collect("trusted_source")
    reader.assert_not_called()
    assert h.audit.report()[0]["event"]["event_type"] == "EVIDENCE_COLLECTION_FAILED"
    assert_no_decision(h, h.boundary.analyze(request(h, [])))


@pytest.mark.parametrize("values", [{}, {"distance": 0}, {"distance": -1},
                                    {"distance": float("nan")}, {"distance": float("inf")},
                                    {"distance": 10, "weight": 5}])
def test_partial_or_invalid_tms_evidence_zero_calls(values):
    connector = TMSReadOnlyConnector()
    connector.analyze_route = Mock(wraps=connector.analyze_route)
    h = make_boundary(kind="tms", connector=connector, values=values,
                      category=Category.TMS_READ_ONLY, capability="tms.route.analyze.read")
    with pytest.raises(EvidenceError):
        h.gate.collect("trusted_source")
    connector.analyze_route.assert_not_called()
    assert_no_decision(h, h.boundary.analyze(request(h, [])))


def test_host_tms_governance_denial_is_preserved():
    governance = AgentGovernanceEngine()
    governance.check_permission = lambda *_: False
    connector = TMSReadOnlyConnector(governance=governance)
    h = make_boundary(kind="tms", connector=connector, category=Category.TMS_READ_ONLY,
                      capability="tms.route.analyze.read")
    with pytest.raises(EvidenceError):
        h.gate.collect("trusted_source")
    assert governance.audit_log[-1]["decision"] == "BLOCK"
    assert_no_decision(h, h.boundary.analyze(request(h, [])))


def test_tms_read_only_and_data_only_payload():
    governance = AgentGovernanceEngine()
    connector = TMSReadOnlyConnector(governance=governance)
    h = make_boundary(kind="tms", connector=connector, category=Category.TMS_READ_ONLY,
                      capability="tms.route.analyze.read")
    result = h.boundary.analyze(request(h))
    assert governance.audit_log[-1]["decision"] == "ALLOW"
    assert result["status"] == "PROPOSED"
    assert result["mode"] == "READ_ONLY"
    assert result["executed"] is result["execution_authorized"] is False
    payload = h.provider.calls[0]
    assert set(payload) == {"instruction", "mode", "evidence"}
    assert set(payload["evidence"][0]) == {"evidence_id", "values"}
    assert payload["evidence"][0]["values"] == {"distance": 100.0}
    assert all(term not in json.dumps(payload) for term in
               ("executed", "executor", "governance", "intelligence", "connector", "tools"))


def test_tms_evidence_cannot_be_substituted_with_direct_telemetry():
    h = make_boundary(category=Category.TMS_READ_ONLY, capability="tms.route.analyze.read")
    assert_no_decision(h, h.boundary.analyze(request(h)))


@pytest.mark.parametrize("capability", ["physical.execution", "warehouse.move_motor"])
def test_physical_execution_zero_calls(capability):
    h = make_boundary(category=Category.PHYSICAL_EXECUTION, capability=capability)
    result = h.boundary.analyze(request(h))
    assert_no_decision(h, result)
    assert result["reason"] == "physical_execution_denied"
    assert result["mode"] == "SIMULATION_ONLY"
    assert h.governance.audit_log == []


@pytest.mark.parametrize("capability", ["physical.simulation_analysis", "warehouse.motor_simulation"])
def test_physical_simulation_analysis_is_simulation_only(capability):
    h = make_boundary(category=Category.PHYSICAL_SIMULATION, capability=capability)
    result = h.boundary.analyze(request(h))
    assert result["status"] == "PROPOSED"
    assert result["mode"] == h.provider.calls[0]["mode"] == "SIMULATION_ONLY"
    assert result["executed"] is result["execution_authorized"] is False


def test_reserved_physical_capability_cannot_be_misclassified():
    with pytest.raises(ValueError, match="capability_category_mismatch"):
        make_boundary(category=Category.READ_ONLY, capability="physical.execution")
    with pytest.raises(ValueError):
        CapabilityPolicy(frozenset({"source"}), "unknown-category")


@pytest.mark.parametrize("field", ["approval", "executed", "execution_authorized", "mode",
                                  "execution_mode", "policy", "policy_override", "tools"])
def test_provider_authority_fields_rejected(field):
    h = make_boundary()
    h.provider.transform = lambda output: {**output, field: True}
    result = h.boundary.analyze(request(h))
    assert_no_decision(h, result, calls=1)
    assert result["reason"] == "invalid_output"
    assert "output_digest" not in h.audit.report()[-1]["event"]


@pytest.mark.parametrize("output", [None, "unstructured", {"summary": float("nan"), "evidence_ids": []},
                                  {"summary": "text", "evidence_ids": ["invented"]}])
def test_invalid_output_never_audited_as_proposal(output):
    h = make_boundary()
    h.provider.transform = lambda _: output
    assert_no_decision(h, h.boundary.analyze(request(h)), calls=1)
    event = h.audit.report()[-1]["event"]
    assert event["status"] == "NO_DECISION"
    assert "output_digest" not in event
    assert "summary" not in event


@pytest.mark.parametrize("field", ["credentials", "approval", "executor", "tools", "execution_mode"])
def test_caller_authority_or_handles_never_cross_boundary(field):
    h = make_boundary()
    assert_no_decision(h, h.boundary.analyze({**request(h), field: object()}))


def test_collection_exception_is_sanitized_and_audited():
    def broken():
        raise RuntimeError(SECRET)
    h = make_boundary(reader=broken)
    with pytest.raises(EvidenceError, match="^invalid_evidence$") as error:
        h.gate.collect("trusted_source")
    assert SECRET not in str(error.value)
    event = h.audit.report()[0]["event"]
    assert set(event) == {"event_type", "stage", "reason", "status", "execution_authorized", "executed"}
    assert SECRET not in json.dumps(h.audit.report())
    assert h.provider.calls == []


class BrokenAudit:
    def record(self, event):
        raise RuntimeError(SECRET)


@pytest.mark.parametrize("audit", [BrokenAudit(), SimpleNamespace(record=lambda _: None)])
def test_audit_failure_blocks_advisory_release(audit):
    h = make_boundary(audit=audit)
    result = h.boundary.analyze(request(h))
    assert_no_decision(h, result, calls=1)
    assert result["reason"] == "audit_unavailable"
    assert result["audit_recorded"] is False
    assert SECRET not in json.dumps(result)


def test_collection_audit_failure_issues_no_reference():
    h = make_boundary(values={}, audit=BrokenAudit())
    with pytest.raises(EvidenceError, match="^audit_unavailable$"):
        h.gate.collect("trusted_source")
    assert_no_decision(h, h.boundary.analyze(request(h, [])))


def test_output_digest_uses_canonical_finite_json():
    h = make_boundary()
    result = h.boundary.analyze(request(h))
    expected = hashlib.sha256(json.dumps(result["analysis"], sort_keys=True,
                                         separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    assert h.audit.report()[-1]["event"]["output_digest"] == expected


def test_runtime_order(monkeypatch):
    h = make_boundary()
    req = request(h)
    order = []
    def observe(obj, name, label):
        original = getattr(obj, name)
        def call(*args, **kwargs):
            order.append(label)
            return original(*args, **kwargs)
        monkeypatch.setattr(obj, name, call)
    observe(h.gate, "check_egress", "capability/egress")
    observe(h.gate, "validate", "evidence")
    observe(h.governance, "authorize_execution", "governance")
    observe(h.provider, "generate", "provider")
    observe(h.boundary, "_valid_output", "output")
    observe(h.guardian, "evaluate", "Guardian")
    observe(h.audit, "record", "audit")
    result = h.boundary.analyze(req)
    order.append("release")
    assert result["status"] == "PROPOSED"
    assert order == ["capability/egress", "evidence", "governance", "provider", "output", "Guardian", "audit", "release"]


def test_guardian_denial_blocks_release():
    h = make_boundary(guardian=SimpleNamespace(evaluate=lambda _: {"action": "INVESTIGATION_REQUIRED"}))
    assert_no_decision(h, h.boundary.analyze(request(h)), calls=1)


def test_provider_error_does_not_fallback_or_leak():
    h = make_boundary()
    fallback = FakeProvider()
    h.router.register("fallback", fallback)
    def broken(_):
        raise RuntimeError(SECRET)
    h.provider.transform = broken
    result = h.boundary.analyze(request(h))
    assert_no_decision(h, result, calls=1)
    assert fallback.calls == []
    assert SECRET not in json.dumps(h.audit.report())
