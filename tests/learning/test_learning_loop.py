from services.learning.learning_loop import LearningLoop


def test_learning():

    engine = LearningLoop()

    result = engine.improve("feedback")

    assert result["improved"] is True
