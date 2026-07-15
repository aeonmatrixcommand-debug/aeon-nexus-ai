from digital_twin.explainability.causal_engine import CausalEngine


def test_causal():

    result = CausalEngine().analyse(
        "cold_chain_breach"
    )

    assert result["cause"] != "Unknown"
    assert len(result["impact_chain"]) > 0
