class RelationshipEngine:
    """
    Build causal relationships.
    """

    def connect(
        self,
        graph,
        event,
        decision,
        outcome
    ):

        event_node = graph.add_node(
            "event",
            event
        )

        decision_node = graph.add_node(
            "decision",
            decision
        )

        outcome_node = graph.add_node(
            "outcome",
            outcome
        )


        graph.add_relationship(
            event_node,
            "caused",
            decision_node
        )

        graph.add_relationship(
            decision_node,
            "produced",
            outcome_node
        )


        return graph.view()
