from typing import Type, TypeVar

from task_manager.domain.entities import Task
from task_manager.domain.ports.repository import IRepository
from task_manager.domain.ports.repository_factory import IRepositoryFactory
from task_manager.repository.in_memory_repositories.task_memrepo import InMemoryTaskRepository

T = TypeVar("T")
K = TypeVar("K")


class MemRepoFactory(IRepositoryFactory):
    def __init__(self, data=[]):
        self.data = data
        self.repos = {
            Type[Task]: InMemoryTaskRepository,
            # Type[User]: InMemoryUserRepository TODO add this repo
        }

    def create_repository(self, type: Type) -> IRepository[T, K]:
        return self.repos[type](self.data)
