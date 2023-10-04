from user import User


class UserRepository:
    def __init__(self):
        self.data = []

    def add_user(self, user: User) -> None:
        """
        Добавление нового пользователя, если он прошел аутентификацию и его не было
        :param user:
        :return:
        """
        if user.is_authenticate and not(self.find_by_name(user.name)):
            self.data.append(user)

    def find_by_name(self, user_name: str) -> bool:
        """
        Поиск пользователя по имени
        :param user_name:
        :return:
        """
        for user in self.data:
            if user.name == user_name:
                return True
        return False
