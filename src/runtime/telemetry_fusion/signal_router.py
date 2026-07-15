from runtime.telemetry_fusion.signal_ingestion import SignalIngestion
from runtime.telemetry_fusion.event_stream import EventStream
from runtime.telemetry_fusion.sensor_fusion import SensorFusion
from runtime.telemetry_fusion.realtime_context import RealTimeContext


class SignalRouter:

    def __init__(self):

        self.ingestion = SignalIngestion()
        self.stream = EventStream()
        self.fusion = SensorFusion()
        self.context = RealTimeContext()


    def process(self, signal):

        received = self.ingestion.ingest(signal)

        self.stream.publish(received)

        fused = self.fusion.combine(
            [signal]
        )

        context = self.context.build(
            fused
        )

        return {
            "received": received,
            "fusion": fused,
            "context": context
        }
