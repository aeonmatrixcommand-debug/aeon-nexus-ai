from enterprise_os.core import AEONEnterpriseOS


os = AEONEnterpriseOS()


event = """
Warehouse DC:
Inventory mismatch detected
Order delay increasing
Driver ETA unstable
"""


sense = os.sense(event)

think = os.think(sense)

decision = os.decide(think)

action = os.act(decision)

learning = os.learn(action)


print("=================================")
print(" AEON MATRIX AUTONOMOUS ENTERPRISE OS ")
print("=================================")

print("\n[SENSE]")
print(sense)

print("\n[THINK]")
print(think)

print("\n[DECIDE]")
print(decision)

print("\n[ACT]")
print(action)

print("\n[LEARN]")
print(learning)

print("\n=================================")
print(" AEON MATRIX CORE SYSTEM ONLINE ")
print(" Sense > Think > Decide > Act > Learn ")
print("=================================")
