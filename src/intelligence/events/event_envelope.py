"""
AEON MATRIX Intelligence Event Envelope
Sprint 79
"""

from dataclasses import dataclass
from datetime import datetime, UTC


@dataclass
class IntelligenceEvent:
    event_type: str
    payload: dict
    created_at: str


def create_event(event_type: str, payload: dict):
    return IntelligenceEvent(
        event_type=event_type,
        payload=payload,
        created_at=datetime.now(UTC).isoformat(),
    )
