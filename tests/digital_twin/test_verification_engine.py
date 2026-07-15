from digital_twin.autonomy.verification_engine import VerificationEngine


def test_verification():

    result = VerificationEngine().verify(
        "reroute_vehicle",
        "sla_recovered"
    )

    assert result["status"] == "confirmed"
