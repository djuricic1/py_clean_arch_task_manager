from uuid import UUID

from task_manager.domain.entities import Task

from task_manager.repository.in_memory_repositories.generic_memrepo import (
    GenericMemRepo,
)


class InMemoryTaskRepository(GenericMemRepo[Task, UUID]):
    ...
