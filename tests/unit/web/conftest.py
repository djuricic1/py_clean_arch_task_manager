from collections.abc import AsyncIterator

import pytest

from task_manager.app import app
from fastapi.testclient import TestClient


async def get_fake_repository_factory() -> AsyncIterator[RepositoryFactory]:
    yield FakeRepositoryFactory()


@pytest.fixture
def app() -> FastAPI:
    testing_app = rest_app
    testing_app.dependency_overrides[
        get_repository_factory
    ] = get_fake_repository_factory

    return testing_app



@pytest.fixture(scope="session")
def test_app():
    yield TestClient(app)

