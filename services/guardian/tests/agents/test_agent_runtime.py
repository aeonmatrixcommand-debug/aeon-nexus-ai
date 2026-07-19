from services.guardian.runtime.agents.coordinator import coordinate
from services.guardian.runtime.agents.performance import evaluate_agent


def test_agent_coordination():

    result = coordinate({
        "task": "Demand Prediction"
    })

    assert result["decision"] == "EXECUTE"


def test_agent_performance():

    result = coordinate({
        "task": "Risk Assessment"
    })

    score = evaluate_agent(result)

    assert score["performance"] == 1.0
