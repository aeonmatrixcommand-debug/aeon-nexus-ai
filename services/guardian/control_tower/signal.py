from dataclasses import dataclass
from datetime import datetime


@dataclass
class RuntimeSignal:
    source: str
    signal_type: str
    severity: str
    value: float
    timestamp: str = datetime.utcnow().isoformat()
