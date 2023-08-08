import abc
from abc import abstractmethod
from datetime import date
from uuid import UUID

from task_manager.domain.entities import Priority, Status, Task


class TaskRepository(abc.ABC):
    @abstractmethod
    def save(
        self,
        title: str,
        description: str,
        due_date: date,
        priority: Priority,
        status: Status,
        assignee_id: UUID,
    ) -> Task:
        ...
