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


def test_user_create_from_dict():
    user_data = {
        "id": uuid4(),
        "username": "alice",
        "email": "alice@example.com",
    }

    user = User.create_from_dict(user_data)

    assert user.id == user_data["id"]
    assert user.username == user_data["username"]
    assert user.email == user_data["email"]


def test_user_to_dict():
    user_id = uuid4()
    username = "john_doe"
    email = "john@example.com"

    user = User(id=user_id, username=username, email=email)

    user_dict = user.to_dict()

    assert user_dict == {"id": user_id, "username": username, "email": email}
