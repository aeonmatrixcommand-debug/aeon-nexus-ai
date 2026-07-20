from services.guardian.governance.learning.learning_policy import validate_learning


def test_policy():
    assert validate_learning(0.9)
