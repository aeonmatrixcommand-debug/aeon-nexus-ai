class KnowledgeReasoner:
    """
    Reason over stored knowledge.
    """

    def analyze(self, knowledge):

        relationships = len(
            knowledge["edges"]
        )

        return {
            "relationships_found": relationships,
            "reasoning_status": "completed"
        }
