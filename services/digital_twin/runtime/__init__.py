from services.digital_twin.offline_engine import OfflineDigitalTwinEngine
from services.digital_twin.twin_confidence import TwinConfidenceEngine
from services.digital_twin.sync_engine import SyncEngine

class DigitalTwinRuntime:
    VERSION = "3.0"

    def status(self):
        return {
            "runtime": "healthy",
            "version": self.VERSION,
            "offline": OfflineDigitalTwinEngine().status(),
            "confidence": TwinConfidenceEngine().calculate(),
            "sync": SyncEngine().synchronize()
        }

if __name__ == "__main__":
    print(DigitalTwinRuntime().status())
