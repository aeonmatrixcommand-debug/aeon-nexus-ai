from digital_twin.memory.cognitive_memory import CognitiveMemory


def test_memory_graph():

    memory = CognitiveMemory()

    result = memory.remember(
        "cold_chain",
        "caused_by",
        "cooling_failure"
    )

    assert result["relation"] == "caused_by"
    assert len(memory.recall()) == 1
