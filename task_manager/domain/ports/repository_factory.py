from typing import Protocol, Type

from task_manager.domain.ports.repository import IRepository


class IRepositoryFactory(Protocol):
    def create_repository(self, type_: Type) -> IRepository:
        raise NotImplementedError()
