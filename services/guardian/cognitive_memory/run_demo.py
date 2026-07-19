from .event_memory.event_store import store as store_event
from .decision_memory.decision_store import store as store_decision
from .outcome_memory.outcome_store import store as store_outcome
from .retrieval.context_retriever import retrieve
from .memory_store.memory_engine import save


event = store_event(
    {
        "type": "INVENTORY_RISK",
        "value": 91
    }
)


decision = store_decision(
    {
        "action": "OPTIMIZE_ALLOCATION"
    }
)


outcome = store_outcome(
    {
        "result": "SUCCESS"
    }
)


context = retrieve(
    "previous inventory decisions"
)


memory = save(
    {
        "event": event,
        "decision": decision,
        "outcome": outcome,
        "context": context
    }
)


print(event)
print(decision)
print(outcome)
print(context)
print(memory)
