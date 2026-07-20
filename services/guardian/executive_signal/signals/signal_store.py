from pathlib import Path
import json


def save_signal(signal):

    with open(
        str(Path(__file__).parent / "executive_signals.json"),
        "a"
    ) as file:
        file.write(json.dumps(signal) + "\n")

    return signal
