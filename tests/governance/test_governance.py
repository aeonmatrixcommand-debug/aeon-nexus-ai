from services.guardian.governance.runtime import GovernanceControl

def test_governance():
    assert GovernanceControl().validate({"action":"execute"})["approved"] is True
