from fastapi import FastAPI

from task_manager.domain.input.task import TaskSaveInput
from task_manager.domain.use_cases.task_use_cases import create_task_use_case
from task_manager.repository.memrepo import MemRepo

app = FastAPI()


@app.post("/task/")
def create_task(task_save_input: TaskSaveInput):
    task_repo = MemRepo([])

    result = create_task_use_case(
        repo=task_repo, task_save_input=task_save_input
    )

    return result
