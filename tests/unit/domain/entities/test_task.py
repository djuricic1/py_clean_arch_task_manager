from datetime import date
from uuid import uuid4

from task_manager.domain.entities.task import Task
from task_manager.domain.enums.task_priority import Priority
from task_manager.domain.enums.task_status import Status


def test_task_init():
    task_id = uuid4()
    title = "Finish Project"
    description = "Complete the project before the deadline."
    due_date = date(2023, 8, 31)
    priority = Priority.HIGH
    status = Status.NOT_STARTED
    assignee_id = uuid4()

    task = Task(
        id=task_id,
        title=title,
        description=description,
        due_date=due_date,
        priority=priority,
        status=status,
        assignee_id=assignee_id,
    )

    assert task.id == task_id
    assert task.title == title
    assert task.description == description
    assert task.due_date == due_date
    assert task.priority == priority
    assert task.status == status
    assert task.assignee_id == assignee_id


def test_task_create_from_dict():
    task_data = {
        "id": uuid4(),
        "title": "Complete Project",
        "description": "Finish the project on time",
        "due_date": date(2023, 8, 31),
        "priority": Priority.HIGH,
        "status": Status.NOT_STARTED,
        "assignee_id": uuid4(),
    }

    task = Task.create_from_dict(task_data)

    assert task.id == task_data["id"]
    assert task.title == task_data["title"]
    assert task.description == task_data["description"]
    assert task.due_date == task_data["due_date"]
    assert task.priority == task_data["priority"]
    assert task.status == task_data["status"]
    assert task.assignee_id == task_data["assignee_id"]


def test_task_to_dict():
    task_id = uuid4()
    title = "Finish Project"
    description = "Complete the project before the deadline."
    due_date = date(2023, 8, 31)
    priority = Priority.HIGH
    status = Status.NOT_STARTED
    assignee_id = uuid4()

    task = Task(
        id=task_id,
        title=title,
        description=description,
        due_date=due_date,
        priority=priority,
        status=status,
        assignee_id=assignee_id,
    )

    task_dict = task.to_dict()

    assert task_dict == {
        "id": task_id,
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": status,
        "assignee_id": assignee_id,
    }
