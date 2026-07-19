class AuditMemory:
    """
    Store AI decision history.
    """

    def __init__(self):
        self.records = []

    def store(self, decision):

        record = {
            "decision": decision,
            "status": "recorded"
        }

        self.records.append(record)

        return record

    def history(self):
        return self.records
