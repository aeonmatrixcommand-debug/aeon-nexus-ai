from value_intelligence.shelf_life import ShelfLifeIntelligence
from value_intelligence.waste_prediction import WastePredictionEngine
from value_intelligence.recovery import ValueRecoveryEngine


shelf = ShelfLifeIntelligence()
waste = WastePredictionEngine()
recovery = ValueRecoveryEngine()


shelf_result = shelf.analyze(5)

waste_result = waste.predict(800)

decision = recovery.recover(
    shelf_result,
    waste_result
)


print("=================================")
print(" AEON MATRIX VALUE RECOVERY AI ")
print("=================================")

print("\nSHELF LIFE INTELLIGENCE")
print(shelf_result)

print("\nWASTE PREDICTION")
print(waste_result)

print("\nVALUE RECOVERY DECISION")
print(decision)

print("\n=================================")
print(" VALUE RECOVERY INTELLIGENCE ONLINE ")
print(" Sense > Predict > Recover > Learn ")
print("=================================")
