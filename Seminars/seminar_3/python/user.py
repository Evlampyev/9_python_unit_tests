class User:
    def __init__(self, name: str, password: str, is_admin=False):
        self.name = name
        self.password = password
        self.is_authenticate = False
        self.is_admin = is_admin

    def authenticate(self, name, password) -> bool:
        if name == self.name and password == self.password:
            self.is_authenticate = True
            return True
        else:
            return False

    def __eq__(self, other):
        if self.name == other.name and self.password == other.password:
            return True
        else:
            return False
