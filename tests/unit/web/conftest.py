import pytest

from collections.abc import AsyncIterator
from uuid import UUID

from fastapi import FastAPI

from task_manager.app import app as web_app
from fastapi.testclient import TestClient

from task_manager.domain.ports.repository import IRepository, T, K
from task_manager.domain.ports.repository_factory import IRepositoryFactory
from task_manager.repository.in_memory_repo_factory import (
    get_repository_factory,
)


class FakeRepository(IRepository[T, UUID]):
    session: list[T]

    def __init__(self, session: list[T] | None):
        self.session = session or []

    def save(self, obj: T) -> T:
        self.session.append(obj)
        return obj

    def get_by_id(self, id_: UUID) -> T:
        ret = next(
            (
                obj
                for obj in self.session
                if obj.id == id_  # type: ignore[attr-defined]
            ),
            None,
        )
        # if not ret:
        #     raise ObjectNotFound(f"Object with id '{id_}' not found")
        return ret

    def get_all(self) -> list[T]:
        return self.session

    def update(self, obj: T, commit: bool = True) -> T:
        item = await self.get_by_id(obj.id)  # type: ignore[attr-defined]

        for name, value in vars(obj).items():
            setattr(item, name, value)

        return item

    def delete(self, id_: UUID) -> bool:
        obj = self.get_by_id(id_)

        return bool(self.session.remove(obj))


class FakeRepositoryFactory:
    def create_repository(self, type_: type) -> IRepository[T, K]:
        return FakeRepository()


async def get_fake_repository_factory() -> AsyncIterator[IRepositoryFactory]:
    yield FakeRepositoryFactory()


@pytest.fixture(scope="session")
def app_overriden() -> FastAPI:
    testing_app: FastAPI = web_app
    testing_app.dependency_overrides[
        get_repository_factory
    ] = get_fake_repository_factory

    return testing_app


@pytest.fixture(scope="session")
def client_test_app(app_overriden):
    yield TestClient(app_overriden)
