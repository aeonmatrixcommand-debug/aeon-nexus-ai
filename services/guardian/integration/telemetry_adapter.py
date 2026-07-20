from services.guardian.runtime.runtime_context import runtime_router


def publish_decision(
    module,
    decision,
    confidence,
    risk
):

    return runtime_router.publish(
        {
            "topic":"guardian.decision",
            "module":module,
            "decision":decision,
            "confidence":confidence,
            "risk":risk
        }
    )
