<<<<<<< HEAD
from .signal.signal_engine import collect
from .kpi.kpi_engine import calculate
from .alert.risk_alert import detect
from .insight.insight_engine import generate
from .report.executive_report import create
from .memory.executive_memory import save
=======
from services.guardian.executive_command_center.signal.signal_engine import collect
from services.guardian.executive_command_center.kpi.kpi_engine import calculate
from services.guardian.executive_command_center.alert.risk_alert import detect
from services.guardian.executive_command_center.insight.insight_engine import generate
from services.guardian.executive_command_center.report.executive_report import create
from services.guardian.executive_command_center.memory.executive_memory import save
>>>>>>> origin/main


signal = collect(
    "AEON_OPERATION_TELEMETRY"
)


kpi = calculate(
    signal
)


alert = detect(
    kpi
)


insight = generate(
    {
        "signal": signal,
        "kpi": kpi,
        "alert": alert
    }
)


report = create(
    {
        "signal": signal,
        "kpi": kpi,
        "alert": alert,
        "insight": insight
    }
)


memory = save(
    report
)


print(signal)
print(kpi)
print(alert)
print(insight)
print(report)
print(memory)
