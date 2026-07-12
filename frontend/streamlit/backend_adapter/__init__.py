from services.guardian.kpi_intelligence.runtime import KPIIntelligence
from services.guardian.real_time_command_center.runtime import RealTimeCommandCenter

def get_command_center_status():
    return {
        "kpi": KPIIntelligence().status(),
        "command_center": RealTimeCommandCenter().status()
    }
