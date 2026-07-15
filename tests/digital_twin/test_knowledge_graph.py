from digital_twin.knowledge.knowledge_graph import KnowledgeGraph


def test_knowledge_graph():

    graph = KnowledgeGraph()

    result = graph.add_entity(
        "warehouse"
    )

    assert result["status"] == "connected"
