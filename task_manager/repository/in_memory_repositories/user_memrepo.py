from uuid import UUID

from task_manager.domain.entities import User

# Just for illustration in-memory storage for now
from task_manager.domain.ports.repository import IRepository


class InMemoryUserRepository(IRepository[User, UUID]):
    def __init__(self, data: list[User]):
        self.data = data

    def save(
        self,
        arg: User,
    ) -> User:
        self.data.append(arg)

        return arg

    def get_all(self) -> list[User]:
        return self.data

    def get_by_id(self, id_: UUID) -> User:
        for d in self.data:
            if d.id == id_:
                return d

    def update(self, arg: User) -> User:
        # TODO add impl
        raise NotImplementedError()

    def delete(self, id_: UUID) -> bool:
        # TODO add impl
        raise NotImplementedError()
