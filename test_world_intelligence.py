from strategic_intelligence.world_signal import WorldSignalIntelligence
from strategic_intelligence.opportunity_radar import OpportunityRadar
from strategic_intelligence.executive_advisor import ExecutiveAIAdvisor


signal = WorldSignalIntelligence()
radar = OpportunityRadar()
advisor = ExecutiveAIAdvisor()


print("=================================")
print(" AEON MATRIX WORLD INTELLIGENCE ")
print("=================================")


signals = signal.collect()

print("\nWORLD SIGNALS")
print(signals)


opportunity = radar.detect(signals)

print("\nOPPORTUNITY RADAR")
print(opportunity)


print("\nEXECUTIVE AI ADVISOR")
print(
    advisor.advise(opportunity)
)


print("\n=================================")
print(" STRATEGIC INTELLIGENCE ONLINE ")
print(" Sense > Understand > Decide > Grow ")
print("=================================")
