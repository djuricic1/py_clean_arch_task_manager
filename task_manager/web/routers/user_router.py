from functools import lru_cache
from typing import Annotated, Type
from uuid import UUID

from fastapi import Depends
from fastapi import APIRouter
from pydantic import BaseModel

from task_manager.domain.entities import User
from task_manager.domain.ports.repository_factory import IRepositoryFactory
from task_manager.repository.in_memory_repo_factory import (
    get_repository_factory,
)

user_router = APIRouter()


class UserPayload(BaseModel):
    username: str
    email: str


@user_router.post("/user/", response_model=None)
def create_user(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    user_payload: UserPayload,
) -> User:
    in_memory_user_repo = repository_factory.create_repository(Type[User])

    result = in_memory_user_repo.save(
        arg=User.create_from_dict(user_payload.model_dump())
    )

    return result


@user_router.get("/user/")
def get_users(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
) -> list[User]:
    in_memory_user_repo = repository_factory.create_repository(Type[User])
    return in_memory_user_repo.get_all()


@user_router.get("/user/{user_id}")
def get_user_by_id(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    user_id: UUID,
) -> User:
    in_memory_user_repo = repository_factory.create_repository(Type[User])
    return in_memory_user_repo.get_by_id(user_id)


@user_router.post("/user/{user_id}")
def update_user_by_id(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    user_id: UUID,
    user_payload: UserPayload,
) -> User:
    in_memory_user_repo = repository_factory.create_repository(Type[User])
    return in_memory_user_repo.update(
        User.create_from_dict(user_payload.model_dump(), user_id=user_id)
    )


@user_router.delete("/user/{user_id}")
def delete_user_by_id(
    repository_factory: Annotated[
        IRepositoryFactory, Depends(get_repository_factory)
    ],
    user_id: UUID,
) -> bool:
    in_memory_user_repo = repository_factory.create_repository(Type[User])
    return in_memory_user_repo.delete(user_id)
