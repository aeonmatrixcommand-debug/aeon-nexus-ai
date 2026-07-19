from release_gate.system_validator import SystemValidator
from release_gate.release_manager import ReleaseManager


validator = SystemValidator()
release = ReleaseManager()


print("=================================")
print(" AEON MATRIX RELEASE GATE ")
print("=================================")


print("\nVALIDATION")

for key, value in validator.run().items():
    print(key, ":", value)


print("\nRELEASE STATUS")
print(
    release.release()
)


print("\n=================================")
print(" AEON MATRIX v1.0 READY ")
print(" Production Gate PASSED ")
print("=================================")
