from services.agent.observability.metrics import (
    LearningMetric,
    LearningMetricsStore,
)
from services.agent.observability.events import (
    LearningEvent,
    LearningEventBus,
)
from services.agent.observability.tracing import (
    LearningTrace,
    LearningTracer,
)


def test_learning_metrics():
    store = LearningMetricsStore()

    store.record(
        LearningMetric(
            agent_id="AEON-001",
            metric="accuracy",
            value=0.98,
        )
    )

    assert store.latest().value == 0.98


def test_learning_events():
    bus = LearningEventBus()

    bus.publish(
        LearningEvent(
            agent_id="AEON-001",
            event_type="learning_update",
            payload={"score": 0.95},
        )
    )

    assert bus.latest().event_type == "learning_update"


def test_learning_trace():
    tracer = LearningTracer()

    tracer.trace(
        LearningTrace(
            agent_id="AEON-001",
            action="policy_update",
            outcome="approved",
        )
    )

    assert tracer.last().outcome == "approved"
