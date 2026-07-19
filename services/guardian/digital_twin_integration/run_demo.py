from .events.event_mapper import map_event
from .sync.twin_sync import TwinSyncEngine
from .executive.situation_room import create_snapshot


event = {
    "type": "STOCK_SHORTAGE"
}


signal = map_event(event)

engine = TwinSyncEngine()

state = engine.update(
    signal["mapped_signal"]
)

print(
    create_snapshot(state)
)
