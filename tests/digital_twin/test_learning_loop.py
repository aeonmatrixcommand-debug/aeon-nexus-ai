from digital_twin.learning.learning_loop import LearningLoop


def test_learning_loop():

    result = LearningLoop().learn(
        "route_optimization_result"
    )

    assert result["status"] == "completed"
