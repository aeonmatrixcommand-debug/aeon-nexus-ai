from src.governance.aegis_policy_engine import AegisPolicyEngine

def test_validate():
    engine = AegisPolicyEngine()
    assert engine.validate({}) is True
