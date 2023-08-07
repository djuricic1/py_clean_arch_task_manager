from dataclasses import dataclass, asdict
from uuid import UUID


@dataclass
class User:
    id: UUID
    username: str
    email: str

    @classmethod
    def create_from_dict(cls, data: dict) -> "User":
        return User(**data)

    def to_dict(self) -> dict:
        return asdict(self)
