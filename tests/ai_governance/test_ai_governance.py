from services.guardian.ai_governance.runtime import AIGovernance

def test_governance():
    assert AIGovernance().validate({})["audit"]
