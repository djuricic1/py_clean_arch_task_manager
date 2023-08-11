from uuid import UUID

from task_manager.domain.entities import Task

from task_manager.domain.ports.repository import IRepository


def create_task_use_case(repo: IRepository, task: Task) -> Task:
    return repo.save(task)


def update_task_use_case(repo: IRepository, task: Task):
    return repo.update(task)


def delete_task_use_case(repo: IRepository, id_: UUID):
    return repo.delete(id_)


def get_tasks(repo: IRepository):
    return repo.get_all()


def get_task(repo: IRepository, id_: UUID):
    return repo.get_by_id(id_)
