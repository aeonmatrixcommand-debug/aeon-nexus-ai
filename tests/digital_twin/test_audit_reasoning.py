from digital_twin.explainability.audit_reasoning import AuditReasoning


def test_audit():

    result = AuditReasoning().record(
        {
            "decision":"move_to_backup_storage",
            "reason":"Risk detected",
            "evidence":[
                "temperature_deviation"
            ]
        }
    )

    assert "timestamp" in result
    assert result["decision"] == "move_to_backup_storage"
