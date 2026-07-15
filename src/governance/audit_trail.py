from datetime import datetime, timezone


class AuditTrail:
    """
    Immutable AI decision record.
    """


    def __init__(self):

        self.records = []


    def record(self, decision):

        entry = {

            "decision": decision,

            "timestamp":
            datetime.now(
                timezone.utc
            ).isoformat(),

            "source":
            "AEON_MATRIX_GOVERNANCE"

        }


        self.records.append(entry)

        return entry


    def history(self):

        return self.records
