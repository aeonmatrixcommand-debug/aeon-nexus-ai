from services.guardian.contracts.ai_runtime_event import AIRuntimeEvent


class RuntimeEventRouter:


    def __init__(self):

        self.telemetry = []
        self.audit = []
        self.gateway = []


    def publish(self,event):

        payload = event.to_dict() if hasattr(event,'to_dict') else event


        self.telemetry.append(payload)

        self.audit.append(payload)

        self.gateway.append(payload)


        return payload
