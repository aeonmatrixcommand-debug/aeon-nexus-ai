from world_intelligence.external_signal import ExternalSignalCollector
from world_intelligence.market_signal import MarketSignalAnalyzer
from world_intelligence.opportunity_detector import OpportunityDetector


class StrategicRadar:

    def __init__(self):

        self.collector = ExternalSignalCollector()
        self.market = MarketSignalAnalyzer()
        self.detector = OpportunityDetector()


    def scan(self, signal):

        external = self.collector.collect(signal)

        analysis = self.market.analyze(
            [external]
        )

        opportunity = self.detector.detect(
            analysis
        )

        return {
            "external_signal": external,
            "market_analysis": analysis,
            "opportunity": opportunity
        }
