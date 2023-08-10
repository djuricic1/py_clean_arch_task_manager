from uuid import UUID

from task_manager.domain.entities import Task
from task_manager.domain.input.task import TaskSaveInput, TaskUpdateInput
from task_manager.domain.ports.task_repository import TaskRepository


def create_task_use_case(
    repo: TaskRepository, task_save_input: TaskSaveInput
) -> Task:
    return repo.save(task_save_input)


def update_task_use_case(
    repo: TaskRepository, task_update_input: TaskUpdateInput
):
    return repo.update(task_update_input)


def delete_task_use_case(
    repo: TaskRepository, id_: UUID
):
    return repo.delete(id_)


def get_tasks(
    repo: TaskRepository
):
    return repo.get_all()


def get_task(
    repo: TaskRepository, id_: UUID
):
    return repo.get_by_id(id_)