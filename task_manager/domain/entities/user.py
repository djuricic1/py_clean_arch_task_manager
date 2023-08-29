from dataclasses import dataclass, asdict
from uuid import UUID


@dataclass
class User:
    id: UUID
    username: str
    email: str

    @classmethod
    def create_from_dict(
            cls, data: dict, user_id: UUID | None = None
    ) -> "User":
        user = User(**data)
        if user_id:
            user.id = user_id
        return user

    def to_dict(self) -> dict:
        return asdict(self)
