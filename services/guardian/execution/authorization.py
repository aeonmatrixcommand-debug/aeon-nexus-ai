from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from uuid import uuid4


@dataclass(frozen=True)
class ExecutionAuthorization:
    """
    Guardian-issued execution authority.

    The authority is bound to one decision and one action.
    V1 provides architectural authority semantics; it is not
    a cryptographically signed security token.
    """

    authorization_id: str
    decision_id: str
    action: str
    issued_by: str
    policy_status: str
    approval_status: str
    issued_at: datetime
    expires_at: datetime


class AuthorizationIssuer:
    ISSUER = "GUARDIAN"

    def issue(
        self,
        *,
        decision_id,
        action,
        policy_status,
        approval_status,
        ttl_seconds=300,
    ):
        if policy_status != "APPROVED":
            raise ValueError("POLICY_NOT_APPROVED")

        if approval_status != "APPROVED":
            raise ValueError("APPROVAL_NOT_APPROVED")

        if not decision_id:
            raise ValueError("DECISION_ID_REQUIRED")

        if not action:
            raise ValueError("ACTION_REQUIRED")

        issued_at = datetime.now(timezone.utc)

        return ExecutionAuthorization(
            authorization_id=str(uuid4()),
            decision_id=decision_id,
            action=action,
            issued_by=self.ISSUER,
            policy_status=policy_status,
            approval_status=approval_status,
            issued_at=issued_at,
            expires_at=issued_at + timedelta(seconds=ttl_seconds),
        )

    def verify(
        self,
        authority,
        *,
        decision_id,
        action,
    ):
        if not isinstance(authority, ExecutionAuthorization):
            return False

        if authority.issued_by != self.ISSUER:
            return False

        if authority.policy_status != "APPROVED":
            return False

        if authority.approval_status != "APPROVED":
            return False

        if authority.decision_id != decision_id:
            return False

        if authority.action != action:
            return False

        now = datetime.now(timezone.utc)

        if authority.expires_at <= now:
            return False

        return True
