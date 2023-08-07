from uuid import uuid4

from task_manager.domain.entities.user import User


def test_user_init():
    user_id = uuid4()
    username = "john_doe"
    email = "john@example.com"

    user = User(id=user_id, username=username, email=email)

    assert user.id == user_id
    assert user.username == username
    assert user.email == email
