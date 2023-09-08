from datetime import date
from typing import Annotated, Type
from uuid import UUID

from fastapi import Depends
from fastapi import APIRouter
from pydantic import BaseModel

from task_manager.domain.entities import Task
from task_manager.domain.enums.task_priority import Priority
from task_manager.domain.enums.task_status import Status
from task_manager.domain.ports.repository_factory import IRepositoryFactory
from task_manager.domain.use_cases.task_use_cases import create_task_use_case
from task_manager.repository.in_memory_repo_factory import (
    get_repository_factory,
)

task_router = APIRouter()


class TaskPayload(BaseModel):
    title: str
    description: str
    due_date: date
    priority: Priority
    status: Status
    assignee_id: UUID


@task_router.post("/task/", response_model=None)
def create_task(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    task_payload: TaskPayload,
) -> Task:
    in_memory_task_repo = repository_factory.create_repository(Type[Task])

    result = create_task_use_case(
        repo=in_memory_task_repo,
        task=Task.create_from_dict(task_payload.model_dump()),
    )

    return result


@task_router.get("/task/")
def get_tasks(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
) -> list[Task]:
    in_memory_task_repo = repository_factory.create_repository(Type[Task])
    return in_memory_task_repo.get_all()


@task_router.get("/task/{task_id}")
def get_task_by_id(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    task_id: UUID,
) -> Task:
    in_memory_task_repo = repository_factory.create_repository(Type[Task])
    return in_memory_task_repo.get_by_id(task_id)


@task_router.post("/task/{task_id}")
def update_task_by_id(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    task_id: UUID,
    task_payload: TaskPayload,
) -> Task:
    in_memory_task_repo = repository_factory.create_repository(Type[Task])
    return in_memory_task_repo.update(
        Task.create_from_dict(task_payload.model_dump(), task_id=task_id)
    )


@task_router.delete("/task/{task_id}")
def delete_task_by_id(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    task_id: UUID,
) -> bool:
    in_memory_task_repo = repository_factory.create_repository(Type[Task])
    return in_memory_task_repo.delete(task_id)
