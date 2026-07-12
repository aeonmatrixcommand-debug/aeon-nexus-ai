from services.autonomous_ops.runtime import AutonomousOperationsRuntime


def test_inventory_execution():

    runtime = AutonomousOperationsRuntime()

    result = runtime.execute_action(
        "inventory_rebalance"
    )

    assert result["status"] == "EXECUTED"
    assert result["impact"] == "STOCK_OPTIMIZED"


def test_sla_recovery():

    runtime = AutonomousOperationsRuntime()

    result = runtime.execute_action(
        "sla_recovery"
    )

    assert result["impact"] == "DELIVERY_RECOVERED"


def test_governance_audit():

    runtime = AutonomousOperationsRuntime()

    log = runtime.governance_log(
        "risk_response"
    )

    assert log["audit"] == "RECORDED"
    assert log["governance"] == "ENABLED"
