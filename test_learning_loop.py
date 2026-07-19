from learning_loop_runtime.memory import EnterpriseMemory
from learning_loop_runtime.self_improvement import SelfImprovementEngine


memory = EnterpriseMemory()
learning = SelfImprovementEngine()


memory.store(
    "Inventory mismatch detected",
    "Auto correction executed"
)

memory.store(
    "ETA instability",
    "Route optimization applied"
)


print("=================================")
print(" AEON MATRIX LEARNING LOOP ")
print("=================================")


print("\nENTERPRISE MEMORY")

for item in memory.recall():
    print(item)


print("\nSELF IMPROVEMENT ENGINE")

print(
    learning.analyze(
        memory.recall()
    )
)


print("\n=================================")
print(" CONTINUOUS LEARNING ONLINE ")
print(" Sense > Learn > Optimize > Improve ")
print("=================================")
