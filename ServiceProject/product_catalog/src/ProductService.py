from .ProductRepository import ProductRepository
import requests

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.user_service_url = "http://localhost:5001/users"
    def get_all_products(self):
        return self.product_repository.get_all()

    def get_product_by_id(self, product_id):
        return self.product_repository.get_by_id(product_id)

    def add_product(self, product_data):
        return self.product_repository.add(product_data)

    def update_product(self, product_id, product_data):
        return self.product_repository.update(product_id, product_data)

    def delete_product(self, product_id):
        return self.product_repository.delete(product_id)
    def validate_user(self, user_id):
        try:
            response = requests.get(f"{self.user_service_url}/{user_id}")
            if response.status_code == 200:
                return True
            return False
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to User Management Service: {e}")
            return False
