from datetime import datetime
from uuid import uuid4


class DecisionAudit:

    def record(self, decision, policy):

        return {
            "audit_id": str(uuid4()),
            "decision": decision.get("decision"),
            "confidence": decision.get("confidence"),
            "policy_status": policy.get("status"),
            "timestamp": datetime.utcnow().isoformat()
        }
