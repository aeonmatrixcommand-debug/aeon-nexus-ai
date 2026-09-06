from integrations.tms import TMSReadOnlyConnector


def test_analyze_route_with_verified_distance():
    result = TMSReadOnlyConnector().analyze_route(
        {"distance": 100}
    )

    assert result["status"] == "OK"
    assert result["mode"] == "READ_ONLY"
    assert result["executed"] is True
    assert result["result"] == {
        "route_status": "optimized",
        "distance": 100.0,
    }
    assert result["audit"]["decision"] == "ALLOW"


def test_missing_distance_produces_no_decision():
    result = TMSReadOnlyConnector().analyze_route({})

    assert result["status"] == "NO_DECISION"
    assert result["executed"] is False
    assert result["reason"] == "positive_numeric_distance_required"
    assert result["axiom"] == "No Evidence -> No Decision"


def test_boolean_distance_is_rejected():
    result = TMSReadOnlyConnector().analyze_route(
        {"distance": True}
    )

    assert result["status"] == "NO_DECISION"
    assert result["executed"] is False
