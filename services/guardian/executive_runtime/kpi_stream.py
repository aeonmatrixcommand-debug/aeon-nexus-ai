class KPIStream:

    def __init__(self):
        self.metrics = {}

    def update(self, key, value):
        self.metrics[key] = value

        return self.metrics


kpi_stream = KPIStream()
