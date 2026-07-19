from ai_gateway.router import AIGateway
from agents_runtime.operations_agent import OperationsAgent
from agents_runtime.logistics_agent import LogisticsAgent
from executive_engine.decision import ExecutiveDecisionEngine


gateway = AIGateway()
ops = OperationsAgent()
logistics = LogisticsAgent()
executive = ExecutiveDecisionEngine()


print("=== AEON MATRIX EXECUTIVE AI ONLINE ===")

data = [
    gateway.route("Warehouse Risk Analysis"),
    ops.analyze("Inventory mismatch + Order delay"),
    logistics.analyze("DC-BKK Route")
]

print("\nAI GATEWAY")
print(data[0])

print("\nMULTI AGENT")
print(data[1])
print(data[2])

print("\nEXECUTIVE DECISION")
print(
    executive.decide(data)
)
