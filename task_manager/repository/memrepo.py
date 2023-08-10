from uuid import uuid4, UUID

from task_manager.domain.entities import Task


# Just for illustration in-memory storage for now
from task_manager.domain.input.task import TaskSaveInput, TaskUpdateInput


class MemRepo:
    def __init__(self, data: list):
        self.data = data

    def save(
        self,
        task_save_input: TaskSaveInput,
    ) -> Task:
        s = 0
        task = Task(uuid4(), **task_save_input.model_dump())

        self.data.append(task)

        return task

    def get_all(self) -> list[Task]:
        return self.data

    def get_by_id(self, id_: UUID) -> Task:
        for d in self.data:
            if d.id == id_:
                return d

    def update(self, task_update_input: TaskUpdateInput) -> Task:
        for d in self.data:
            if d.id == task_update_input.id_:
                d = Task(id=d.id,
                         **task_update_input)
                break

    def delete(self, id_: UUID) -> bool:
        try:
            self.data.pop()
        except Exception as ex:
            # TODO add new exception type here
            raise ex
        return True
