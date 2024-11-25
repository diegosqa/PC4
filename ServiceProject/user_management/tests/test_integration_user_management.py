import pytest
from user_management.src.UserController import app



@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_create_user(client):
    response = client.post('/users', json={"name": "Sebastian Amao", "email": "sebastian.amao@example.com"})
    assert response.status_code == 201
    assert response.get_json()["message"] == "User created"

def test_get_all_users(client):
    client.post('/users', json={"name": "Sebastian Amao", "email": "sebastian.amao@example.com"})
    response = client.get('/users')
    users = response.get_json()
    assert len(users) > 0
    assert users[0]["name"] == "Sebastian Amao"

def test_get_user_by_id(client):
    client.post('/users', json={"name": "Sebastian Amao", "email": "sebastian.amao@example.com"})
    response = client.get('/users/1')
    user = response.get_json()
    assert user["name"] == "Sebastian Amao"

def test_update_user(client):
    client.post('/users', json={"name": "Sebastian Amao", "email": "sebastian.amao@example.com"})
    response = client.put('/users/1', json={"email": "updated.email@example.com"})
    assert response.status_code == 200
    assert response.get_json()["message"] == "User updated"

def test_delete_user(client):
    client.post('/users', json={"name": "Sebastian Amao", "email": "sebastian.amao@example.com"})
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.get_json()["message"] == "User deleted"

# Escenarios adicionales
def test_get_nonexistent_user(client):
    response = client.get('/users/99')
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"

def test_update_nonexistent_user(client):
    response = client.put('/users/99', json={"email": "new.email@example.com"})
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"

def test_delete_nonexistent_user(client):
    response = client.delete('/users/99')
    assert response.status_code == 404
    assert response.get_json()["error"] == "User not found"
