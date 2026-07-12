from services.guardian.enterprise_memory.runtime import EnterpriseMemory

def test_memory():
    assert EnterpriseMemory().store("event")["stored"]
