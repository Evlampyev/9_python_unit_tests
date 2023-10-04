import unittest
from user import User
from user_repository import UserRepository


class TestUserRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.user = User('Test_name', 'Test_password')
        self.users = UserRepository()

    def test_add_user(self):
        self.user.authenticate('Test_name', 'Test_password')
        self.users.add_user(self.user)
        result = False
        for user in self.users.data:
            if user == User('Test_name', 'Test_password'):
                result = True
        self.assertTrue(result)

    def test_not_add_user(self):
        self.user.authenticate('Test_name', 'Test_password')
        self.users.add_user(self.user)
        result = False
        for user in self.users.data:
            if user == User('Test_name', 'Not_test_password'):
                result = True
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
