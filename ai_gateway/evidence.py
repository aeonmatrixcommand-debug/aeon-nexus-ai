"""Evidence references issued only from host-configured, trusted collectors.

Collectors, source policies, and the clock are trusted application configuration,
never request/model input. A collector's honesty cannot be established by numeric
validation: the host must verify its provenance. Caller-provided facts, timestamps,
and claims of verification are never accepted as evidence by the boundary.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import json
import math
from threading import Lock
from typing import Callable, Mapping
from uuid import uuid4

from integrations.tms import TMSReadOnlyConnector
from ai_gateway.audit import configured_audit
from src.governance.immutable_audit import AuditReceipt


class EvidenceError(ValueError):
    pass


@dataclass(frozen=True)
class EvidenceSource:
    # Reader returns {"observed_at": aware datetime, "values": {metric: number}}.
    reader: Callable[[], Mapping]
    required_metrics: frozenset[str]
    allowed_metrics: frozenset[str]
    classification: str = "INTERNAL"
    kind: str = "telemetry"

    def __post_init__(self):
        object.__setattr__(self, "required_metrics", frozenset(self.required_metrics))
        object.__setattr__(self, "allowed_metrics", frozenset(self.allowed_metrics))
        if self.kind not in {"telemetry", "tms"}:
            raise ValueError("unsupported_source_kind")
        if (not self.required_metrics
                or not self.required_metrics <= self.allowed_metrics
                or any(type(metric) is not str or not metric for metric in self.allowed_metrics)):
            raise ValueError("unsupported_source_metrics")
        # The existing connector supports exactly one route measurement.
        if self.kind == "tms" and not (
                self.required_metrics == self.allowed_metrics == {"distance"}):
            raise ValueError("unsupported_tms_metrics")
        if self.classification not in {"PUBLIC", "INTERNAL", "CONFIDENTIAL", "RESTRICTED"}:
            raise ValueError("unsupported_classification")


class EvidenceGate:
    def __init__(self, sources: Mapping[str, EvidenceSource], *,
                 max_age: timedelta = timedelta(minutes=5),
                 clock: Callable[[], datetime] | None = None,
                 tms_connector: TMSReadOnlyConnector | None = None, audit=None, audit_mode=None):
        if max_age <= timedelta(0):
            raise ValueError("positive_max_age_required")
        self.__sources = dict(sources)
        self.__records: dict[str, str] = {}
        self.__lock = Lock()
        self.__max_age = max_age
        self.__clock = clock or (lambda: datetime.now(timezone.utc))
        # Host-owned dependency, never constructed here or exposed in evidence.
        if tms_connector is not None and not isinstance(tms_connector, TMSReadOnlyConnector):
            raise TypeError("governed_read_only_connector_required")
        self.__tms_connector = tms_connector
        self.__audit = configured_audit(audit, mode=audit_mode)

    def require_durable_audit(self):
        """Host composition check; does not expose the sink or connector."""
        configured_audit(self.__audit, mode="production")

    def collect(self, source: str) -> str:
        """Host-side ingestion; never a provider tool. Mint an opaque reference.

        Invalid readings never receive a reference. Every collection failure attempts
        a sanitized audit append, independently of later analyze() calls. If logging
        fails, no reference is issued and audit_unavailable is raised.
        """
        try:
            spec = self.__sources[source]
            if spec.kind == "tms" and self.__tms_connector is None:
                raise EvidenceError("invalid_evidence")
            reading = spec.reader()
            if set(reading) != {"observed_at", "values"}:
                raise EvidenceError("invalid_evidence")
            observed_at = reading["observed_at"]
            if not isinstance(observed_at, datetime) or observed_at.utcoffset() is None:
                raise EvidenceError("invalid_evidence")
            values = self._values(reading["values"], spec)
            if spec.kind == "tms":
                # Never export the connector, its identity, audit, or intelligence.
                result = self.__tms_connector.analyze_route(values)
                if (result.get("status") != "OK" or result.get("mode") != "READ_ONLY"
                        or result.get("audit", {}).get("decision") != "ALLOW"):
                    raise EvidenceError("invalid_evidence")
                values = self._values({"distance": result["result"]["distance"]}, spec)
            record = json.dumps({
                "source": source, "observed_at": observed_at.isoformat(),
                "values": values, "kind": spec.kind,
                "classification": spec.classification,
            }, allow_nan=False)
            reference = uuid4().hex
            with self.__lock:
                self.__records[reference] = record
            return reference
        except Exception:
            try:
                receipt = self.__audit.record({
                    "event_type": "EVIDENCE_COLLECTION_FAILED",
                    "stage": "evidence_collection", "reason": "invalid_evidence",
                    "status": "NO_DECISION",
                    "execution_authorized": False, "executed": False,
                })
                if not isinstance(receipt, AuditReceipt) or not receipt.audit_id:
                    raise RuntimeError("audit_ack_required")
            except Exception:
                raise EvidenceError("audit_unavailable") from None
            raise EvidenceError("invalid_evidence") from None

    def check_egress(self, references, *, sources, classifications):
        records = self._resolve(references)
        if any(r["source"] not in sources or r["classification"] not in classifications
               for r in records):
            raise EvidenceError("egress_denied")

    def validate(self, references) -> list[dict]:
        records = self._resolve(references)
        now = self.__clock()
        for record in records:
            age = now - datetime.fromisoformat(record["observed_at"])
            if age < timedelta(0) or age > self.__max_age:
                raise EvidenceError("invalid_evidence")
            self._values(record["values"], self.__sources[record["source"]])
        return records

    def _resolve(self, references) -> list[dict]:
        if (type(references) is not list or not references or len(references) > 100
                or any(type(ref) is not str for ref in references)
                or len(set(references)) != len(references)):
            raise EvidenceError("invalid_evidence")
        try:
            with self.__lock:
                return [{"evidence_id": ref, **json.loads(self.__records[ref])}
                        for ref in references]
        except KeyError:
            raise EvidenceError("invalid_evidence") from None

    @staticmethod
    def _values(values, spec) -> dict:
        if (type(values) is not dict
                or not spec.required_metrics <= set(values) <= spec.allowed_metrics):
            raise EvidenceError("invalid_evidence")
        if any(type(v) not in {int, float} or not math.isfinite(v) for v in values.values()):
            raise EvidenceError("invalid_evidence")
        if spec.kind == "tms" and values.get("distance", 0) <= 0:
            raise EvidenceError("invalid_evidence")
        return dict(values)
