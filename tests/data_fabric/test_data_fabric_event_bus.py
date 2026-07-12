from services.data_fabric.runtime import EnterpriseEventBus


def test_publish_event():

    bus = EnterpriseEventBus()

    event = bus.publish(
        "WMS_STOCK_UPDATE",
        {
            "sku": "A001",
            "qty": 100
        }
    )

    assert event["type"] == "WMS_STOCK_UPDATE"
    assert event["status"] == "RECEIVED"


def test_consume_latest():

    bus = EnterpriseEventBus()

    bus.publish(
        "TMS_ROUTE_UPDATE",
        {
            "route": "R001"
        }
    )

    result = bus.consume_latest()

    assert result["type"] == "TMS_ROUTE_UPDATE"


def test_governance():

    bus = EnterpriseEventBus()

    bus.publish(
        "AI_DECISION",
        {
            "action": "OPTIMIZE"
        }
    )

    log = bus.governance_log()

    assert log["audit"] == "ENABLED"
    assert log["event_count"] == 1
