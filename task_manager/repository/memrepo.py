from uuid import UUID

from task_manager.domain.entities import Task


# Just for illustration in-memory storage for now
from task_manager.domain.ports.repository import IRepository


class InMemoryTaskRepository(IRepository[Task, UUID]):
    def __init__(self, data: list[Task]):
        self.data = data

    def save(
        self,
        arg: Task,
    ) -> Task:
        self.data.append(arg)

        return arg

    def get_all(self) -> list[Task]:
        return self.data

    def get_by_id(self, id_: UUID) -> Task:
        for d in self.data:
            if d.id == id_:
                return d

    def update(self, arg: Task) -> Task:
        # TODO add impl
        raise NotImplementedError()

    def delete(self, id_: UUID) -> bool:
        # TODO add impl
        raise NotImplementedError()
