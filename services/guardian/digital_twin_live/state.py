from dataclasses import dataclass
from datetime import datetime


@dataclass
class TwinState:

    warehouse: str
    inventory: int
    demand: int
    risk: float
    timestamp: str = datetime.utcnow().isoformat()
