from strategic_intelligence.signal_collector import SignalCollector
from strategic_intelligence.opportunity_radar import OpportunityRadar



class StrategicRuntime:


    def __init__(self):

        self.collector = SignalCollector()
        self.radar = OpportunityRadar()



    def analyze(self):


        signals = self.collector.collect()


        opportunities = self.radar.analyze(
            signals
        )


        return {

            "signals":
            signals,

            "intelligence":
            opportunities,

            "status":
            "strategic_ready"

        }
