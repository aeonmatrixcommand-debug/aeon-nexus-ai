from services.digital_twin.runtime import DigitalTwinRuntime
from services.guardian.real_time_command_center.runtime import RealTimeCommandCenter


class RuntimeGateway:

    def __init__(self):
        self.digital_twin = DigitalTwinRuntime()
        self.command_center = RealTimeCommandCenter()

    def health(self):
        return {
            "platform": "AEON MATRIX",
            "digital_twin": self.digital_twin.status(),
            "command_center": "ONLINE"
        }

    def system_status(self):
        return self.health()
