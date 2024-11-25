from user_management.src.UserRepository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_users(self):
        return self.user_repository.get_all()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def add_user(self, user_data):
        return self.user_repository.add(user_data)

    def update_user(self, user_id, user_data):
        return self.user_repository.update(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)
