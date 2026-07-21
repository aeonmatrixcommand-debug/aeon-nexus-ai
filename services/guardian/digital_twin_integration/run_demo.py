<<<<<<< HEAD
from .events.event_mapper import map_event
from .sync.twin_sync import TwinSyncEngine
from .executive.situation_room import create_snapshot
=======
from services.guardian.digital_twin_integration.events.event_mapper import map_event
from services.guardian.digital_twin_integration.sync.twin_sync import TwinSyncEngine
from services.guardian.digital_twin_integration.executive.situation_room import create_snapshot
>>>>>>> 1df4713 (fix: migrate guardian imports to services namespace)


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
