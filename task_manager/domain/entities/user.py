from dataclasses import dataclass, asdict
from uuid import UUID


@dataclass
class User:
    id: UUID
    username: str
    email: str

    def to_dict(self) -> dict:
        return asdict(self)