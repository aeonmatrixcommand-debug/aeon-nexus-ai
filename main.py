import sys
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from bootstrap.startup import startup

print("=" * 50)
print("AEON MATRIX Enterprise AI Platform")
print("=" * 50)

startup()

print("\nSystem Status : READY")
