from datetime import date
from uuid import UUID, uuid4

from task_manager.domain.entities import Priority, Status, Task


# Just for illustration in memory storage
class MemRepo:
    def __init__(self, data: list):
        self.data = data

    def save(
        self,
        title: str,
        description: str,
        due_date: date,
        priority: Priority,
        status: Status,
        assignee_id: UUID,
    ) -> Task:
        task = Task(
            uuid4(),
            title,
            description,
            due_date,
            priority,
            status,
            assignee_id,
        )

        self.data.append(task)

        return task
