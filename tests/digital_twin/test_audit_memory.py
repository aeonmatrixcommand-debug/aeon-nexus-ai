from digital_twin.governance.audit_memory import AuditMemory


def test_audit_memory():

    memory = AuditMemory()

    result = memory.store(
        "optimize_route"
    )

    assert result["status"] == "recorded"
    assert len(memory.history()) == 1
