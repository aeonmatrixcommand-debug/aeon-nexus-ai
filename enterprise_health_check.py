import importlib
import pkgutil
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(".")
SERVICES = ROOT / "services"

print("=" * 70)
print("AEON NEXUS AI - ENTERPRISE HEALTH CHECK")
print("=" * 70)

passed = 0
failed = 0
errors = []

if SERVICES.exists():
    for _, name, _ in pkgutil.walk_packages([str(SERVICES)], "services."):
        try:
            importlib.import_module(name)
            print(f"[PASS] {name}")
            passed += 1
        except Exception as e:
            print(f"[FAIL] {name} -> {e}")
            failed += 1
            errors.append((name, str(e)))
else:
    print("services/ directory not found")
    sys.exit(1)

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"PASS : {passed}")
print(f"FAIL : {failed}")

print("\nCompiling Python files...")
subprocess.run([sys.executable, "-m", "compileall", "services"])

if pathlib.Path("tests").exists():
    print("\nRunning pytest...")
    subprocess.run([sys.executable, "-m", "pytest", "-q"])

if errors:
    print("\nFAILED MODULES")
    print("=" * 70)
    for name, err in errors:
        print(f"{name}\n  {err}\n")
