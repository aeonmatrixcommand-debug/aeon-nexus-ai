from datetime import datetime, timedelta, timezone

import pytest


def _authority_module():
    from services.guardian.execution.authorization import (
        ExecutionAuthorization,
        AuthorizationIssuer,
    )
    return ExecutionAuthorization, AuthorizationIssuer


def test_issuer_creates_authority_bound_to_decision_and_action():
    ExecutionAuthorization, AuthorizationIssuer = _authority_module()

    issuer = AuthorizationIssuer()

    authority = issuer.issue(
        decision_id="decision-001",
        action="ALLOCATE_STOCK",
        policy_status="APPROVED",
        approval_status="APPROVED",
    )

    assert isinstance(authority, ExecutionAuthorization)
    assert authority.authorization_id
    assert authority.decision_id == "decision-001"
    assert authority.action == "ALLOCATE_STOCK"
    assert authority.issued_by == "GUARDIAN"
    assert authority.policy_status == "APPROVED"
    assert authority.approval_status == "APPROVED"


def test_authority_for_different_action_is_invalid():
    _, AuthorizationIssuer = _authority_module()

    issuer = AuthorizationIssuer()

    authority = issuer.issue(
        decision_id="decision-001",
        action="ALLOCATE_STOCK",
        policy_status="APPROVED",
        approval_status="APPROVED",
    )

    assert not issuer.verify(
        authority,
        decision_id="decision-001",
        action="CHANGE_ROUTE",
    )


def test_authority_for_different_decision_is_invalid():
    _, AuthorizationIssuer = _authority_module()

    issuer = AuthorizationIssuer()

    authority = issuer.issue(
        decision_id="decision-001",
        action="ALLOCATE_STOCK",
        policy_status="APPROVED",
        approval_status="APPROVED",
    )

    assert not issuer.verify(
        authority,
        decision_id="decision-999",
        action="ALLOCATE_STOCK",
    )


def test_expired_authority_is_invalid():
    _, AuthorizationIssuer = _authority_module()

    issuer = AuthorizationIssuer()

    authority = issuer.issue(
        decision_id="decision-001",
        action="ALLOCATE_STOCK",
        policy_status="APPROVED",
        approval_status="APPROVED",
        ttl_seconds=-1,
    )

    assert not issuer.verify(
        authority,
        decision_id="decision-001",
        action="ALLOCATE_STOCK",
    )


def test_non_authority_object_is_invalid():
    _, AuthorizationIssuer = _authority_module()

    issuer = AuthorizationIssuer()

    forged = {
        "authorization_id": "fake",
        "decision_id": "decision-001",
        "action": "ALLOCATE_STOCK",
        "issued_by": "GUARDIAN",
    }

    assert not issuer.verify(
        forged,
        decision_id="decision-001",
        action="ALLOCATE_STOCK",
    )


def test_issuer_refuses_nonapproved_policy():
    _, AuthorizationIssuer = _authority_module()

    issuer = AuthorizationIssuer()

    with pytest.raises(ValueError):
        issuer.issue(
            decision_id="decision-001",
            action="ALLOCATE_STOCK",
            policy_status="BLOCK",
            approval_status="APPROVED",
        )


def test_issuer_refuses_nonapproved_approval():
    _, AuthorizationIssuer = _authority_module()

    issuer = AuthorizationIssuer()

    with pytest.raises(ValueError):
        issuer.issue(
            decision_id="decision-001",
            action="ALLOCATE_STOCK",
            policy_status="APPROVED",
            approval_status="DENIED",
        )
