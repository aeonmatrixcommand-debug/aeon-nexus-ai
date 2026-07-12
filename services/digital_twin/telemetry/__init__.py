class TelemetryEngine:
    def ingest(self):
        return {"status":"streaming"}

    def health(self):
        return {"service":"telemetry","status":"healthy"}
