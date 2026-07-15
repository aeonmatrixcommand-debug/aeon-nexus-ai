from digital_twin.memory.situation_memory import SituationMemory
from digital_twin.causal.causal_graph import CausalGraph
from digital_twin.communication.ai_explanation import AIExplanation
from digital_twin.communication.human_alignment import HumanAlignment
from digital_twin.adaptive_dashboard.dashboard_optimizer import DashboardOptimizer


def test_cognitive_layer():

    memory = SituationMemory()
    memory.store("cold_chain_breach")

    graph = CausalGraph().analyse(
        "cold_chain_breach"
    )

    explanation = AIExplanation().explain(graph)

    report = HumanAlignment().create_report(
        explanation
    )

    dashboard = DashboardOptimizer().generate(
        "critical"
    )

    assert len(memory.recall()) == 1
    assert report["approval_required"] is True
    assert "risk" in dashboard
