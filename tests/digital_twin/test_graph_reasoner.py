from digital_twin.knowledge.graph_reasoner import GraphReasoner


def test_graph_reasoning():

    result = GraphReasoner().analyse(
        "warehouse"
    )

    assert result["insight"] == "generated"
