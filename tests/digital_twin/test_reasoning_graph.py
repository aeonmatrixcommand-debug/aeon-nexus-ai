from digital_twin.memory.reasoning_graph import ReasoningGraph


def test_reasoning_graph():

    result = ReasoningGraph().infer(
        [
            {
                "source": "rain",
                "relation": "causes",
                "target": "traffic"
            },
            {
                "source": "traffic",
                "relation": "causes",
                "target": "delay"
            }
        ]
    )

    assert result["status"] == "generated"
