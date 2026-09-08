"""Process-local append-only snapshots, not tamper-proof durable storage.

The host owns this trusted sink. Production persistence/retention is a separate
deployment requirement. Production durability: NOT ESTABLISHED. This is neither
durable, WORM, tamper-proof, nor restart-safe storage.
"""

from datetime import datetime, timezone
import hashlib
import json
from threading import Lock
from uuid import uuid4


from src.governance.audit_event import AuditReceipt


class ImmutableAudit:
    def __init__(self):
        self.__entries: list[bytes] = []
        self.__lock = Lock()

    def append(self, event: dict) -> AuditReceipt:
        # Serialize before storing: neither inputs nor returned history alias it.
        snapshot = json.dumps(event, sort_keys=True, allow_nan=False)
        with self.__lock:
            audit_id = uuid4().hex
            sequence = len(self.__entries) + 1
            encoded = json.dumps({
                "audit_id": audit_id,
                "sequence": sequence,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "event": json.loads(snapshot),
            }, sort_keys=True, allow_nan=False).encode("utf-8")
            receipt = AuditReceipt(
                audit_id, sequence, hashlib.sha256(encoded).hexdigest()
            )
            self.__entries.append(encoded)
            return receipt

    def history(self) -> list[dict]:
        with self.__lock:
            return [json.loads(entry) for entry in self.__entries]
