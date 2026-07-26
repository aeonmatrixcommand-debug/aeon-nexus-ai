"""
AEON MATRIX Mother Brain Launcher
"""

from src.intelligence.mother_brain.runtime import MotherBrainRuntime


def main():
    runtime = MotherBrainRuntime()

    print("=" * 40)
    print(" AEON MATRIX MOTHER BRAIN ONLINE ")
    print("=" * 40)

    signal = "Inventory mismatch detected"

    result = runtime.process(signal)

    print(f"Signal      : {result.signal}")
    print(f"Action      : {result.action}")
    print(f"Confidence  : {result.confidence:.2f}")

    print("=" * 40)
    print(" Sense > Think > Decide > Act ")
    print("=" * 40)


if __name__ == "__main__":
    main()
