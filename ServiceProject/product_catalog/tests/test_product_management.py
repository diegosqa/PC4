import pytest
from product_catalog.src.ProductRepository import ProductRepository



@pytest.fixture
def product_repo():
    return ProductRepository()

def test_add_product(product_repo):
    product = {"name": "Laptop", "price": 2500.00}
    result = product_repo.add(product)
    assert result["id"] == 1
    assert result["name"] == "Laptop"

def test_get_product_by_id(product_repo):
    product_repo.add({"name": "Laptop", "price": 2500.00})
    product = product_repo.get_by_id(1)
    assert product["name"] == "Laptop"

def test_update_product(product_repo):
    product_repo.add({"name": "Laptop", "price": 2500.00})
    updated = product_repo.update(1, {"price": 2800.00})
    assert updated is True
    assert product_repo.get_by_id(1)["price"] == 2800.00

def test_delete_product(product_repo):
    product_repo.add({"name": "Laptop", "price": 2500.00})
    deleted = product_repo.delete(1)
    assert deleted is True
    assert product_repo.get_by_id(1) is None

# Escenarios adicionales
def test_add_multiple_products(product_repo):
    product1 = product_repo.add({"name": "Laptop", "price": 2500.00})
    product2 = product_repo.add({"name": "Mouse", "price": 50.00})
    assert product1["id"] == 1
    assert product2["id"] == 2

def test_get_nonexistent_product(product_repo):
    product = product_repo.get_by_id(99)
    assert product is None

def test_delete_nonexistent_product(product_repo):
    deleted = product_repo.delete(99)
    assert deleted is False
