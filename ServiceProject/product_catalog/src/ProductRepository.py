class ProductRepository:
    def __init__(self):
        self.products = {}  # Simulando base de datos en memoria
        self.current_id = 1

    def get_all(self):
        return list(self.products.values())

    def get_by_id(self, product_id):
        return self.products.get(product_id)

    def add(self, product_data):
        product_data['id'] = self.current_id
        self.products[self.current_id] = product_data
        self.current_id += 1
        return product_data

    def update(self, product_id, product_data):
        if product_id in self.products:
            self.products[product_id].update(product_data)
            return True
        return False

    def delete(self, product_id):
        return self.products.pop(product_id, None) is not None

