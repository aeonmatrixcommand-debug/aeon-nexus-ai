from digital_twin.adaptive.learning_engine import LearningEngine


def test_learning():

    result = LearningEngine().learn(
        [
            "cold_chain_breach",
            "capacity_shortage"
        ]
    )

    assert result["learning_status"] == "active"
