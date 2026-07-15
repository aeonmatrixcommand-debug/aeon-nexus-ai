from digital_twin.autonomy.decision_orchestrator import DecisionOrchestrator


def test_orchestrator():

    result = DecisionOrchestrator().run(
        "cold_chain_risk"
    )

    assert result["status"] == "completed"
