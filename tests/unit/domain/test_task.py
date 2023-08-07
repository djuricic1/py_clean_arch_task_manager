from datetime import date
from uuid import uuid4

from task_manager.domain.entities.task import Task, Priority, Status


def test_task_init():
    task_id = uuid4()
    title = "Finish Project"
    description = "Complete the project before the deadline."
    due_date = date(2023, 8, 31)
    priority = Priority.HIGH
    status = Status.NOT_STARTED
    assignee_id = uuid4()

    task = Task(id=task_id, title=title, description=description, due_date=due_date,
                priority=priority, status=status, assignee_id=assignee_id)

    assert task.id == task_id
    assert task.title == title
    assert task.description == description
    assert task.due_date == due_date
    assert task.priority == priority
    assert task.status == status
    assert task.assignee_id == assignee_id
