from digital_twin.world_signal.signal_collector import SignalCollector
from digital_twin.world_signal.signal_intelligence import SignalIntelligence
from digital_twin.world_signal.opportunity_engine import OpportunityEngine


class WorldSignalRuntime:
    """
    Connect world signals with Digital Twin.
    """

    def __init__(self):

        self.collector = SignalCollector()
        self.intelligence = SignalIntelligence()
        self.opportunity = OpportunityEngine()


    def execute(self, signals):

        collected = self.collector.collect(signals)

        insights = self.intelligence.analyze(
            collected
        )

        opportunities = self.opportunity.detect(
            insights
        )

        return {
            "signals": collected,
            "insights": insights,
            "opportunities": opportunities
        }
