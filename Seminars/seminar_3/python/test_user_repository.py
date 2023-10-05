import unittest
from user import User
from user_repository import UserRepository


class TestUserRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.user = User('Test_name', 'Test_password')
        self.user_1 = User('Admin', 'Test_admin_password', True)
        self.user_2 = User('Next_user', 'Test_next_password')
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

    def test_log_out(self):
        self.user.authenticate('Test_name', 'Test_password')
        self.users.add_user(self.user)
        self.user_1.authenticate('Admin', 'Test_admin_password')
        self.users.add_user(self.user_1)
        self.user_2.authenticate('Next_user', 'Test_next_password')
        self.users.add_user(self.user_2)
        result = True
        self.users.log_out()
        for user in self.users.data:
            if not user.is_admin:
                result = False
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
