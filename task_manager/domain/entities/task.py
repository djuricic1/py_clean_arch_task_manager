import datetime
from dataclasses import dataclass, asdict
from enum import Enum
from uuid import UUID


class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Status(Enum):
    NOT_STARTED = "Not started"
    IN_PROGRESS = "In progress"
    COMPLETED = "Completed"


@dataclass
class Task:
    id: UUID
    title: str
    description: str
    due_date: datetime.date
    priority: Priority
    status: Status
    assignee_id: UUID

    def to_dict(self) -> dict:
        return asdict(self)
