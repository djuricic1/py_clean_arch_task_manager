from task_manager.domain.entities import Task
from task_manager.domain.enums import Priority, Status


task_payload_data = {
    "title": "Test Task",
    "description": "This is a test task",
    "due_date": "2023-09-08",
    "priority": Priority.HIGH,
    "status": Status.IN_PROGRESS,
    "assignee_id": "550e8400-e29b-41d4-a716-446655440000",
}


def test_create_task(client_test_app):
    response = client_test_app.post("/task/", json=task_payload_data)
    assert response.status_code == 200
    task = Task(**response.json())
    expected_task = Task(**task_payload_data)

    assert task.title == expected_task.title
    assert task.description == expected_task.description
    assert task.due_date == expected_task.due_date
    assert task.priority == expected_task.priority
    assert task.status == expected_task.status
    assert task.assignee_id == expected_task.assignee_id
