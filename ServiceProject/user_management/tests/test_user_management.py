import pytest
from user_management.src.UserRepository import UserRepository

@pytest.fixture
def user_repo():
    return UserRepository()

def test_add_user(user_repo):
    user = {"name": "Sebastian Amao", "email": "sebastian.amao@example.com"}
    result = user_repo.add(user)
    assert result["id"] == 1
    assert result["name"] == "Sebastian Amao"

def test_get_user_by_id(user_repo):
    user_repo.add({"name": "Sebastian Amao", "email": "sebastian.amao@example.com"})
    user = user_repo.get_by_id(1)
    assert user["name"] == "Sebastian Amao"

def test_update_user(user_repo):
    user_repo.add({"name": "Sebastian Amao", "email": "sebastian.amao@example.com"})
    updated = user_repo.update(1, {"email": "new.email@example.com"})
    assert updated is True
    assert user_repo.get_by_id(1)["email"] == "new.email@example.com"

def test_delete_user(user_repo):
    user_repo.add({"name": "Sebastian Amao", "email": "sebastian.amao@example.com"})
    deleted = user_repo.delete(1)
    assert deleted is True
    assert user_repo.get_by_id(1) is None

# Escenarios adicionales
def test_add_multiple_users(user_repo):
    user1 = user_repo.add({"name": "User 1", "email": "user1@example.com"})
    user2 = user_repo.add({"name": "User 2", "email": "user2@example.com"})
    assert user1["id"] == 1
    assert user2["id"] == 2

def test_get_nonexistent_user(user_repo):
    user = user_repo.get_by_id(99)
    assert user is None

def test_delete_nonexistent_user(user_repo):
    deleted = user_repo.delete(99)
    assert deleted is False
