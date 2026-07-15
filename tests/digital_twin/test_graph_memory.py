from digital_twin.knowledge.graph_memory import GraphMemory


def test_graph_memory():

    memory = GraphMemory()

    result = memory.remember(
        "warehouse_capacity_change"
    )

    assert result["stored"] is True
