import datetime
from dataclasses import dataclass, asdict, field
from uuid import UUID, uuid4

from task_manager.domain.enums import Priority
from task_manager.domain.enums import Status


@dataclass
class Task:
    title: str
    description: str
    due_date: datetime.date
    priority: Priority
    status: Status
    assignee_id: UUID
    id: UUID = field(default_factory=uuid4)

    @classmethod
    def create_from_dict(
        cls, data: dict, task_id: UUID | None = None
    ) -> "Task":
        task = Task(**data)
        if task_id:
            task.id = task_id
        return task

    def to_dict(self) -> dict:
        return asdict(self)
