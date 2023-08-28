from datetime import date
from functools import lru_cache
from typing import Annotated, Type
from uuid import UUID

from fastapi import FastAPI, Depends

from task_manager.domain.entities import Task
from task_manager.domain.enums.task_priority import Priority
from task_manager.domain.enums.task_status import Status
from task_manager.domain.ports.repository_factory import IRepositoryFactory
from task_manager.domain.use_cases.task_use_cases import create_task_use_case
from task_manager.repository.in_memory_repo_factory import MemRepoFactory

rest_app = FastAPI()


@lru_cache
def get_repository_factory() -> IRepositoryFactory:
    return MemRepoFactory([])


@rest_app.post("/task/", response_model=None)
def create_task(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
) -> Task:
    in_memory_task_repo = repository_factory.create_repository(Type[Task])

    random_task = Task(
        id=UUID("b4c57439-bde0-461e-b811-c37f7abe21a0"),
        title="Complete Project Report",
        description="Write a detailed project report for the quarterly review.",
        due_date=date(2023, 8, 25),
        priority=Priority.HIGH,
        status=Status.IN_PROGRESS,
        assignee_id=UUID("b4c57439-bde0-461e-b811-c37f7abe21a0"),
    )

    result = create_task_use_case(repo=in_memory_task_repo, task=random_task)

    return result


@rest_app.get("/task/")
def get_tasks(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
) -> list[Task]:
    in_memory_task_repo = repository_factory.create_repository(Type[Task])
    return in_memory_task_repo.get_all()


@rest_app.get("/task/{task_id}")
def get_task_by_id(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    task_id: UUID,
):
    in_memory_task_repo = repository_factory.create_repository(Type[Task])
    return in_memory_task_repo.get_by_id(task_id)


@rest_app.post("/task/{task_id}")
def update_task_by_id(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    task_id: UUID,
):
    random_task = Task(
        id=UUID("b4c57439-bde0-461e-b811-c37f7abe21a0"),
        title="Complete Project Report",
        description="Write a detailed project report for the quarterly review.",
        due_date=date(2023, 8, 25),
        priority=Priority.HIGH,
        status=Status.COMPLETED,
        assignee_id=UUID("b4c57439-bde0-461e-b811-c37f7abe21a0"),
    )

    in_memory_task_repo = repository_factory.create_repository(Type[Task])
    return in_memory_task_repo.update(random_task)


@rest_app.delete("/task/{task_id}")
def delete_task_by_id(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    task_id: UUID,
):
    in_memory_task_repo = repository_factory.create_repository(Type[Task])
    return in_memory_task_repo.delete(task_id)
