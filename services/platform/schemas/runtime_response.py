from dataclasses import dataclass


@dataclass
class RuntimeResponse:
    service: str
    status: str
    message: str
