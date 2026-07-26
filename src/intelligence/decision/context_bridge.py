"""
AEON MATRIX Decision Context Bridge
Sprint 79.9
"""


class DecisionContextBridge:
    """
    Enriches Mother Brain decisions
    with Digital Twin intelligence.
    """

    def enrich(self, twin_context):

        return {
            "entity": twin_context.entity_id,
            "state": twin_context.operational_state,
            "confidence": twin_context.confidence,
            "simulation": twin_context.simulation_result,
        }
