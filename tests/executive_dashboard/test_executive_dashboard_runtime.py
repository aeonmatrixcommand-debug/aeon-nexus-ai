from services.executive_dashboard.runtime import ExecutiveDashboardRuntime

def test_dashboard_summary():
    runtime = ExecutiveDashboardRuntime()
    summary = runtime.summary()

    assert summary["platform"] == "AEON MATRIX"
    assert summary["status"] == "ONLINE"
    assert len(summary["modules"]) >= 5
