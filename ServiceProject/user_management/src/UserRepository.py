class UserRepository:
    def __init__(self):
        self.users = {}  # Simulando base de datos en memoria
        self.current_id = 1

    def get_all(self):
        return list(self.users.values())

    def get_by_id(self, user_id):
        return self.users.get(user_id)

    def add(self, user_data):
        user_data['id'] = self.current_id
        self.users[self.current_id] = user_data
        self.current_id += 1
        return user_data

    def update(self, user_id, user_data):
        if user_id in self.users:
            self.users[user_id].update(user_data)
            return True
        return False

    def delete(self, user_id):
        return self.users.pop(user_id, None) is not None
