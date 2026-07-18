import json
from pathlib import Path


class AuditStore:

    FILE = Path("guardian_audit.json")

    def save(self, record):

        data = []

        if self.FILE.exists():
            data = json.loads(
                self.FILE.read_text()
            )

        data.append(record)

        self.FILE.write_text(
            json.dumps(
                data,
                indent=2
            )
        )

        return record


    def load(self):

        if not self.FILE.exists():
            return []

        return json.loads(
            self.FILE.read_text()
        )
