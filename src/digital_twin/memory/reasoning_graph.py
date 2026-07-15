class ReasoningGraph:
    """
    Infer knowledge from relationships.
    """

    def infer(self, graph):

        if len(graph) >= 2:

            return {
                "inference": "relationship_detected",
                "status": "generated"
            }

        return {
            "inference": "insufficient_data",
            "status": "pending"
        }
