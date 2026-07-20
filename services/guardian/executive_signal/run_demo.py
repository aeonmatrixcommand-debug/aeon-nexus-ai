from pathlib import Path

SIGNAL_FILE = Path(__file__).parent / "signals/executive_signals.json"

from .engine.signal_engine import ExecutiveSignalEngine
from .signals.signal_store import save_signal
from .dashboard.dashboard_feed import create_dashboard_feed


decision = {
    "decision": "ESCALATE_TO_EXECUTIVE",
    "risk_score": 91
}


engine = ExecutiveSignalEngine()

signal = engine.generate(decision)

save_signal(signal)

print(create_dashboard_feed(signal))
