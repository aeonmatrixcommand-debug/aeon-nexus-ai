"""
AEON MATRIX Release Check
"""

from pathlib import Path

FILES = [
    "services/mother_brain.py",
    "services/guardian/matrix_core.py",
    "src/intelligence/mother_brain/runtime.py",
    "release/RC1_MANIFEST.md",
]

print("=" * 50)
print("AEON MATRIX RELEASE CHECK")
print("=" * 50)

missing = []

for file in FILES:
    if Path(file).exists():
        print(f"[OK] {file}")
    else:
        print(f"[MISSING] {file}")
        missing.append(file)

print("=" * 50)

if missing:
    print("STATUS : FAILED")
    raise SystemExit(1)

print("STATUS : RELEASE CANDIDATE READY")
