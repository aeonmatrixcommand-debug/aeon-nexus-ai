"""
AEON MATRIX Telemetry Pipeline
"""


from services.guardian.telemetry.event_bus import publish
from services.guardian.telemetry.event_processor import process


def ingest(event):

    publish_result = publish(event)
    analysis = process(event)

    return {
        "ingestion": publish_result,
        "analysis": analysis
    }
