from services.guardian.autonomous_os.event_mesh import EventMesh
from services.guardian.autonomous_os.recovery_engine import RecoveryEngine
from services.guardian.autonomous_os.learning_governance import LearningGovernance


class AutonomousOperatingSystem:

    def __init__(self):
        self.mesh = EventMesh()
        self.recovery = RecoveryEngine()
        self.learning = LearningGovernance()

    def process(self, event):

        stream = self.mesh.publish(
            "guardian.runtime",
            event
        )

        return {
            "event": stream,
            "recovery": self.recovery.analyze(event),
            "learning": self.learning.validate(event)
        }
