from datetime import date
from uuid import UUID

from pydantic import BaseModel

from task_manager.domain.entities import Status, Priority


class TaskSaveInput(BaseModel):
    title: str
    description: str
    due_date: date
    priority: Priority
    status: Status
    assignee_id: UUID


class TaskUpdateInput(TaskSaveInput):
    id_: UUID


class TaskDeleteInput:
    id: UUID
