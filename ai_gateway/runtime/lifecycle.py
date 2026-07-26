from datetime import datetime


class LifecycleManager:

    STATES = [
        "PLANNED",
        "APPROVED",
        "EXECUTING",
        "COMPLETED",
        "VERIFIED",
        "FAILED"
    ]


    def __init__(self):
        self.transitions=[]


    def move(self, state):

        event={
            "state": state,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.transitions.append(event)

        return event


    def history(self):
        return self.transitions
