from digital_twin.decision.confidence_engine import ConfidenceEngine


def test_confidence():

    result = ConfidenceEngine().calculate(
        {
            "action": "move_to_backup_storage"
        }
    )

    assert result["confidence"] > 0.9
