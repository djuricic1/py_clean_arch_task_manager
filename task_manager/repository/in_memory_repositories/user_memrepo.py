from uuid import UUID

from task_manager.domain.entities import User

from task_manager.repository.in_memory_repositories.generic_memrepo import (
    GenericMemRepo,
)


class InMemoryUserRepository(GenericMemRepo[User, UUID]):
    ...
