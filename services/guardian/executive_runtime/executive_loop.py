from services.guardian.executive_runtime.kpi_stream import kpi_stream


def publish_decision(result):

    return kpi_stream.update(
        "active_decision",
        result["decision"]
    )
