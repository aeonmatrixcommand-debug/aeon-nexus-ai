
from services.agents.memory.memory_store import AgentMemoryStore
from services.agents.memory.memory_context import AgentMemoryContext


def test_agent_memory_save():

    store = AgentMemoryStore()

    store.save(
        "wms-agent",
        {
            "event": "inventory_check"
        }
    )

    memories = store.get(
        "wms-agent"
    )

    assert len(memories) == 1


def test_agent_memory_context():

    store = AgentMemoryStore()

    store.save(
        "sales-agent",
        {
            "intent": "promotion"
        }
    )

    context = AgentMemoryContext(
        store
    )

    result = context.build_context(
        "sales-agent",
        {
            "customer": "china"
        }
    )

    assert result["agent_id"] == "sales-agent"
    assert len(result["history"]) == 1

