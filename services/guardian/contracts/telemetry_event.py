from dataclasses import dataclass


@dataclass
class TelemetryEvent:

    topic: str
    payload: dict
