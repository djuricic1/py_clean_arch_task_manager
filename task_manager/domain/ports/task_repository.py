from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from task_manager.domain.entities import Task
from task_manager.domain.input.task import TaskSaveInput, TaskUpdateInput


class TaskRepository(Protocol):
    @abstractmethod
    def save(self, task_save_input: TaskSaveInput) -> Task:
        ...

    @abstractmethod
    def get_all(self) -> list[Task]:
        ...

    @abstractmethod
    def get_by_id(self, id_: UUID) -> Task:
        ...

    @abstractmethod
    def update(self, task_update_input: TaskUpdateInput) -> Task:
        ...

    @abstractmethod
    def delete(self, id_: UUID) -> bool:
        ...
