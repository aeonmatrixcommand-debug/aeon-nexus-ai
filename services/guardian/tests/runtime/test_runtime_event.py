from services.guardian.contracts.ai_runtime_event import AIRuntimeEvent


def test_event_trace():

    e=AIRuntimeEvent(
        "Guardian",
        "Forecast",
        "DECISION",
        "ALLOCATE",
        .94
    )

    assert e.trace_id
