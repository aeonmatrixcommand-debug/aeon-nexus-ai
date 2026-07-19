from world_intelligence.signal_engine import WorldSignalEngine
from strategic_ai.opportunity_radar import OpportunityRadar
from strategic_ai.executive_engine import StrategicDecisionEngine


signal_engine = WorldSignalEngine()
radar = OpportunityRadar()
executive = StrategicDecisionEngine()


signals = signal_engine.collect(
    [
        "market demand increase",
        "logistics disruption",
        "waste reduction opportunity"
    ]
)


opportunity = radar.analyze(signals)

decision = executive.decide(opportunity)


print("=== AEON MATRIX STRATEGIC AI ONLINE ===")

print("\nWORLD SIGNAL")
print(signals)

print("\nOPPORTUNITY RADAR")
print(opportunity)

print("\nEXECUTIVE STRATEGY")
print(decision)
