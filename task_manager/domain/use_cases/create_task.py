from datetime import date
from uuid import UUID

from task_manager.domain.entities import Priority, Status, Task
from task_manager.domain.ports.task_repository import TaskRepository


def create_task_use_case(
    repo: TaskRepository,
    title: str,
    description: str,
    due_date: date,
    priority: Priority,
    status: Status,
    assignee_id: UUID,
) -> Task:

    result = repo.save(
        title, description, due_date, priority, status, assignee_id
    )

    return result
