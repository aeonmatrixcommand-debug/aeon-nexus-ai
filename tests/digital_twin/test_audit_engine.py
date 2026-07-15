from digital_twin.governance.audit_engine import AuditEngine


def test_audit():

    result = AuditEngine().record(
        "optimize_route",
        {
            "status":"success"
        }
    )

    assert "timestamp" in result
