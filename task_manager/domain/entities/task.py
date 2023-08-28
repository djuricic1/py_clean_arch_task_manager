import datetime
from dataclasses import dataclass, asdict
from uuid import UUID

from task_manager.domain.enums import Priority
from task_manager.domain.enums import Status


@dataclass
class Task:
    id: UUID
    title: str
    description: str
    due_date: datetime.date
    priority: Priority
    status: Status
    assignee_id: UUID

    @classmethod
    def create_from_dict(cls, data: dict) -> "Task":
        return Task(**data)

    def to_dict(self) -> dict:
        return asdict(self)
