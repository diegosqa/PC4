import pytest
from product_catalog.src.ProductController import app



@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_create_product(client):
    response = client.post('/products', json={"name": "Laptop", "price": 2500.00})
    assert response.status_code == 201
    assert response.get_json()["message"] == "Product created"

def test_get_all_products(client):
    client.post('/products', json={"name": "Laptop", "price": 2500.00})
    response = client.get('/products')
    products = response.get_json()
    assert len(products) > 0
    assert products[0]["name"] == "Laptop"

def test_get_product_by_id(client):
    client.post('/products', json={"name": "Laptop", "price": 2500.00})
    response = client.get('/products/1')
    product = response.get_json()
    assert product["name"] == "Laptop"

def test_update_product(client):
    client.post('/products', json={"name": "Laptop", "price": 2500.00})
    response = client.put('/products/1', json={"price": 2800.00})
    assert response.status_code == 200
    assert response.get_json()["message"] == "Product updated"

def test_delete_product(client):
    client.post('/products', json={"name": "Laptop", "price": 2500.00})
    response = client.delete('/products/1')
    assert response.status_code == 200
    assert response.get_json()["message"] == "Product deleted"

# Escenarios adicionales
def test_get_nonexistent_product(client):
    response = client.get('/products/99')
    assert response.status_code == 404
    assert response.get_json()["error"] == "Product not found"

def test_update_nonexistent_product(client):
    response = client.put('/products/99', json={"price": 2800.00})
    assert response.status_code == 404
    assert response.get_json()["error"] == "Product not found"

def test_delete_nonexistent_product(client):
    response = client.delete('/products/99')
    assert response.status_code == 404
    assert response.get_json()["error"] == "Product not found"
