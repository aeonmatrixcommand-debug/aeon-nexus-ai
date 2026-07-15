from digital_twin.cognition.explanation_engine import ExplanationEngine


def test_explanation():

    result = ExplanationEngine().explain(
        "cold_chain_risk",
        "temperature anomaly",
        "product_loss_risk"
    )

    assert result["explanation_status"] == "generated"
