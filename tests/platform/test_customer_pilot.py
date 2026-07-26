from src.aeon_platform.customer.pilot_manager import (
    PilotManager,
)

from src.aeon_platform.customer.feedback_engine import (
    FeedbackEngine,
)

from src.aeon_platform.customer.success_metrics import (
    SuccessMetrics,
)


def test_pilot():

    pilot = PilotManager().start(
        "customer001"
    )

    assert pilot.phase == "pilot"


def test_feedback():

    result = FeedbackEngine().analyze(
        [
            "faster delivery",
            "better visibility",
        ]
    )

    assert result["insight_generated"]


def test_success():

    result = SuccessMetrics().calculate(
        {
            "OTIF": 95,
            "SLA": 98,
        }
    )

    assert result["health_score"] > 0
